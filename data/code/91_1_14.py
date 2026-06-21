class BooleanOperator:
    @classmethod
    def validate_input(cls, value: bool) -> bool:
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean type")
        return value

    @classmethod
    def negate(cls, value: bool) -> bool:
        validated = cls.validate_input(value)
        return not validated

if __name__ == '__main__':
    operator = BooleanOperator()
    true_result = operator.negate(True)
    false_result = operator.negate(False)
    print(true_result)
    print(false_result)