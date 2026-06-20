class BooleanNegator:
    @classmethod
    def validate_input(cls, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
    
    @classmethod
    def negate(cls, value):
        cls.validate_input(value)
        return not value

if __name__ == '__main__':
    negator_instance = BooleanNegator()
    result1 = negator_instance.negate(True)
    result2 = negator_instance.negate(False)
    print(result1)
    print(result2)