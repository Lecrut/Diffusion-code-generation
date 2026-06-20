class DataValidator:
    def __init__(self, data: str):
        self.raw_data = data

    def clean_input(self) -> str:
        if not isinstance(self.raw_data, str):
            raise TypeError("Input must be a string")
        return self.raw_data.strip()

if __name__ == '__main__':
    validator = DataValidator("   hello world   ")
    result = validator.clean_input()
    print(result)