class StringValidator:
    @staticmethod
    def contains_only_digits_and_spaces(input_string):
        return input_string.isdigit() or (input_string.replace(' ', '').isdigit())

if __name__ == '__main__':
    validator = StringValidator()
    sample_string1 = "12345"
    sample_string2 = "123 456"
    sample_string3 = "abc123"

    print(f"Input: {sample_string1}, Result: {validator.contains_only_digits_and_spaces(sample_string1)}")
    print(f"Input: {sample_string2}, Result: {validator.contains_only_digits_and_spaces(sample_string2)}")
    print(f"Input: {sample_string3}, Result: {validator.contains_only_digits_and_spaces(sample_string3)}")