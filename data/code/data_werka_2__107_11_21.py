class DateConverter:
    FORMAT_INPUT = "%m/%d/%Y"
    FORMAT_OUTPUT = "%Y-%m-%d"

    @staticmethod
    def _validate_and_parse(date_str):
        parts = date_str.split('/')
        if len(parts) != 3:
            raise ValueError("Invalid format")
        month, day, year = (int(p) for p in parts)
        if not (1 <= month <= 12 and 1 <= day <= 31 and 1 <= year <= 9999):
            raise ValueError("Invalid components")
        return year, month, day

    @staticmethod
    def convert(date_str):
        year, month, day = DateConverter._validate_and_parse(date_str)
        return f"{year:04d}-{month:02d}-{day:02d}"

if __name__ == '__main__':
    print(DateConverter.convert("01/15/2024"))
    print(DateConverter.convert("12/31/1999"))