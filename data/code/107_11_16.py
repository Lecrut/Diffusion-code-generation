class DateConverter:
    def __init__(self, separator_in: str = '/', separator_out: str = '-'):
        self.separator_in = separator_in
        self.separator_out = separator_out

    def convert(self, date_str: str) -> str:
        parts = date_str.split(self.separator_in)
        if len(parts) != 3:
            raise ValueError("Invalid date format")
        month, day, year = int(parts[0]), int(parts[1]), int(parts[2])
        return f"{year}-{month:02d}-{day:02d}"

if __name__ == '__main__':
    converter = DateConverter()
    result1 = converter.convert("01/15/2024")
    result2 = converter.convert("12/25/2023")
    print(result1)
    print(result2)