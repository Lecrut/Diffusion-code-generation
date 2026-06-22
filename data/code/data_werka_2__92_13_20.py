from typing import Union

class LogicalInverter:
    def __init__(self):
        self._truth = True

    def __call__(self, value: bool) -> bool:
        if not isinstance(value, bool):
            raise ValueError("Expected boolean type")
        return value ^ self._truth

if __name__ == '__main__':
    inverter = LogicalInverter()
    print(inverter(True))
    print(inverter(False))
    print(not inverter(True))
    print(inverter(1 == 1))
    print(inverter(1 != 1))
    try:
        inverter(None)
    except ValueError as e:
        print("Validated error")
    print(inverter(True) is False)
    print(inverter(False) is True)