class BooleanNegator:
    @classmethod
    def validate_input(cls, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
    
    @classmethod
    def negate(cls, value: bool) -> bool:
        cls.validate_input(value)
        return not value

if __name__ == '__main__':
    negator = BooleanNegator()
    print(negator.negate(True))
    print(negator.negate(False))