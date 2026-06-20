class InputValidator:
    def is_valid_input(self, input_string):
        return bool(input_string) and input_string.isalpha()

if __name__ == '__main__':
    validator = InputValidator()
    sample_strings = ["Hello", "", "123", "World!", "Python"]
    for string in sample_strings:
        print(f"'{string}': {validator.is_valid_input(string)}")