from typing import Union

CONVERSION_FACTOR = 12

class LengthConverter:
    def __init__(self, feet_value: float) -> None:
        self._feet_value = feet_value

    def to_inches(self) -> Union[int, float]:
        return self._feet_value * CONVERSION_FACTOR

if __name__ == '__main__':
    first_converter = LengthConverter(3)
    second_converter = LengthConverter(2.5)
    third_converter = LengthConverter(0.5)
    print(first_converter.to_inches())
    print(second_converter.to_inches())
    print(third_converter.to_inches())