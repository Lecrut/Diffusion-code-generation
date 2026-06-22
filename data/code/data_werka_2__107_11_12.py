class DateFormatter:
    def __init__(self, input_format: str = "%m/%d/%Y", output_format: str = "%Y-%m-%d"):
        self.input_format = input_format
        self.output_format = output_format

    def format(self, date_string: str) -> str:
        parts = date_string.split("/")
        if len(parts) != 3:
            raise ValueError("Date string must contain exactly three parts separated by slashes")
        month_str, day_str, year_str = parts
        month = int(month_str)
        day = int(day_str)
        year = int(year_str)
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
        if not (1 <= day <= 31):
            raise ValueError("Day must be between 1 and 31")
        if year < 1:
            raise ValueError("Year must be positive")
        return f"{year:04d}-{month:02d}-{day:02d}"

if __name__ == '__main__':
    formatter = DateFormatter()
    result1 = formatter.format("01/15/2024")
    print(result1)
    result2 = formatter.format("12/31/1999")
    print(result2)