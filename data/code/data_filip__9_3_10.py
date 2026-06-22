class StringValidator:
    def clean_input(self, user_input):
        if not isinstance(user_input, str):
            raise TypeError("Input must be a string")
        return user_input.strip()

if __name__ == '__main__':
    validator = StringValidator()
    test_string = "   Hello World   "
    cleaned_result = validator.clean_input(test_string)
    print(cleaned_result)
    another_test = "\t\tTrimmed\t\t"
    print(validator.clean_input(another_test))