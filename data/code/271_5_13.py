class StringValidator:
    @staticmethod
    def contains_only_digits_and_spaces(input_string):
        return input_string.isdigit() or all(char == ' ' for char in input_string)

if __name__ == '__main__':
    validator = StringValidator()
    sample_string1 = "12345"
    sample_string2 = "12 34"
    sample_string3 = "abcde"

    print(f"Input: {sample_string1}, Result: {validator.contains_only_digits_and_spaces(sample_string1)}")
    print(f"Input: {sample_string2}, Result: {validator.contains_only_digits_and_spaces(sample_string2)}")
    print(f"Input: {sample_string3}, Result: {validator.contains_only_digits_and_spaces(sample_string3)}")