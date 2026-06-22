from typing import Final

class BooleanNegationLogic:
    FALSE: Final[bool] = False
    TRUE: Final[bool] = True

    @staticmethod
    def _check_type(value: object) -> bool:
        if not isinstance(value, bool):
            raise ValueError(f"Expected bool, got {type(value).__name__}")
        return value

    @classmethod
    def negate(cls, value: object) -> bool:
        validated = cls._check_type(value)
        return cls.TRUE if validated is cls.FALSE else cls.FALSE

if __name__ == '__main__':
    val_true: bool = BooleanNegationLogic.negate(True)
    val_false: bool = BooleanNegationLogic.negate(False)
    print(val_true)
    print(val_false)