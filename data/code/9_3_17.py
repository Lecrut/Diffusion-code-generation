class DataValidator:
    def clean_input_string(self, value):
        if not isinstance(value, str):
            return ""
        return value.strip()

if __name__ == '__main__':
    validator = DataValidator()
    result = validator.clean_input_string("  hello world  ")
    print(repr(result))