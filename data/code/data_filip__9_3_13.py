class DataValidator:
    def clean_input(self, user_input):
        if not isinstance(user_input, str):
            raise TypeError("Input must be a string")
        return user_input.strip()

if __name__ == '__main__':
    validator = DataValidator()
    sample_inputs = [
        "  hello world  ",
        "\t\nData Science\t\n",
        "  ",
        "no_whitespace",
        "\r\n\n\t  spaces and tabs  \t\n\r"
    ]
    for sample in sample_inputs:
        cleaned = validator.clean_input(sample)
        print(repr(cleaned))