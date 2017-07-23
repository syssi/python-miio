from .device import Device
from typing import Any, Dict


class Strip(Device):
    """Main class representing the smart strip."""

    def on(self):
        """Power on."""
        return self.send("set_power", ["on"])

    def off(self):
        """Power off."""
        return self.send("set_power", ["off"])

    def status(self):
        """Retrieve properties."""
        properties = ['power', 'temperature', 'current', 'mode']
        values = self.send(
            "get_prop",
            properties
        )
        return StripStatus(dict(zip(properties, values)))

    def set_power_mode(self, mode: str):
        """Set mode."""

        # green, normal
        return self.send("set_power_mode", [mode])


class StripStatus:
    """Container for status reports from the strip."""
    def __init__(self, data: Dict[str, Any]) -> None:
        self.data = data

    @property
    def power(self) -> str:
        return self.data["power"]

    @property
    def is_on(self) -> bool:
        return self.power == "on"

    @property
    def temperature(self) -> float:
        return self.data["temperature"]

    @property
    def current(self) -> float:
        return self.data["current"]

    @property
    def mode(self) -> float:
        return self.data["mode"]

    def __str__(self) -> str:
        s = "<StripStatus power=%s, temperature=%s, " \
            "current=%s mode=%s>" % \
            (self.power, self.temperature,
             self.current, self.mode)
        return s
