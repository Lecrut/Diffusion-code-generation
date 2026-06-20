class BooleanValidator:
    valid_values = {'true', 'false', '1', '0'}

    def is_valid(self, value):
        return value.lower() in self.valid_values

if __name__ == '__main__':
    validator = BooleanValidator()
    test_values = ['True', 'false', '1', '0', 'yes', 'no']
    for value in test_values:
        print(f"'{value}' is valid: {validator.is_valid(value)}")