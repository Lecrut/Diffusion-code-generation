class BooleanNegator:
    @classmethod
    def is_valid_input(cls, value):
        return isinstance(value, bool)

    @classmethod
    def negate(cls, value: bool) -> bool:
        if not cls.is_valid_input(value):
            raise ValueError("Input must be a boolean")
        return not value

if __name__ == '__main__':
    negator = BooleanNegator()
    print(negator.negate(True))
    print(negator.negate(False))