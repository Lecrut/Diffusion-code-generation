class InputValidator:
    def is_valid_input(self, string):
        return bool(string) and string.isalpha()

if __name__ == '__main__':
    validator = InputValidator()
    sample_values = ["Hello", "", "123", "Python3"]
    for value in sample_values:
        result = validator.is_valid_input(value)
        print(f"'{value}' is valid: {result}")