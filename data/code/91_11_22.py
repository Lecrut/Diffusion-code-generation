class LogicalInverter:
    def __init__(self, flag: bool) -> None:
        self._active = flag

    def invert(self) -> bool:
        if self._active is True:
            self._active = False
            return False
        if self._active is False:
            self._active = True
            return True
        raise ValueError("Attribute must be a boolean type")

    def get_status(self) -> bool:
        return self._active

if __name__ == '__main__':
    inverter = LogicalInverter(True)
    new_state = inverter.invert()
    print(new_state)
    print(inverter.get_status())
    inverter.invert()
    print(inverter.get_status())