class DataValidator:
    def __init__(self):
        self.errors = []

    def clean_input(self, value):
        if not isinstance(value, str):
            raise TypeError("Input must be a string")
        return value.strip()

if __name__ == '__main__':
    validator = DataValidator()
    raw_string = "   hello world   "
    cleaned = validator.clean_input(raw_string)
    print(cleaned)