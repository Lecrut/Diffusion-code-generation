class StringValidator:
    @staticmethod
    def contains_only_digits_and_spaces(input_string):
        return input_string.isalnum() and all(char.isdigit() or char.isspace() for char in input_string)

if __name__ == '__main__':
    validator = StringValidator()
    sample_string1 = "12345"
    sample_string2 = "123 456"
    sample_string3 = "abc123"
    
    print(f"Input String: {sample_string1}, Valid: {validator.contains_only_digits_and_spaces(sample_string1)}")
    print(f"Input String: {sample_string2}, Valid: {validator.contains_only_digits_and_spaces(sample_string2)}")
    print(f"Input String: {sample_string3}, Valid: {validator.contains_only_digits_and_spaces(sample_string3)}")