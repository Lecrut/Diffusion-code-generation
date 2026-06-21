from typing import ClassVar

class BooleanInverter:
    FALSE_VAL: ClassVar[int] = 0
    TRUE_VAL: ClassVar[int] = 1
    BIT_MASK: ClassVar[int] = 1

    @staticmethod
    def invert(value: bool) -> bool:
        raw: int = int(value)
        toggled: int = (raw ^ BooleanInverter.BIT_MASK)
        return bool(toggled)

if __name__ == '__main__':
    print(BooleanInverter.invert(True))
    print(BooleanInverter.invert(False))