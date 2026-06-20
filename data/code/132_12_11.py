class BooleanValidator:
    def is_valid(self, value: str) -> bool:
        normalized_value = value.lower()
        return normalized_value in {'true', 'false', '1', '0'}

if __name__ == '__main__':
    validator = BooleanValidator()
    test_values = ['True', 'false', '1', '0', 'yes', 'no']
    for value in test_values:
        print(f"'{value}' is valid: {validator.is_valid(value)}")