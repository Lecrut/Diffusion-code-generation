class BooleanValidator:
    TRUE_VALUES = {'true', '1'}
    FALSE_VALUES = {'false', '0'}

    @staticmethod
    def is_valid_boolean(value: str) -> bool:
        normalized_value = value.lower()
        return normalized_value in BooleanValidator.TRUE_VALUES or normalized_value in BooleanValidator.FALSE_VALUES
if __name__ == '__main__':
    print(BooleanValidator.is_valid_boolean('True'))
    print(BooleanValidator.is_valid_boolean('false'))
    print(BooleanValidator.is_valid_boolean('1'))
    print(BooleanValidator.is_valid_boolean('0'))
    print(BooleanValidator.is_valid_boolean('yes'))
    print(BooleanValidator.is_valid_boolean('no'))