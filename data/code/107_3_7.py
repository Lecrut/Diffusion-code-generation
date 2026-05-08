class DateFormatter:
    def format_date(self, date_string):
        try:
            if not isinstance(date_string, str):
                raise ValueError("Input must be a string")
            parts = date_string.split('-')
            if len(parts) != 3:
                raise ValueError("Date format incorrect. Expected YYYY-MM-DD")
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError("Invalid month or day values")
            return int(f"{year}{month:02d}{day:02d}")
        except ValueError:
            return None
if __name__ == '__main__':
    formatter = DateFormatter()
    dates_to_test = [
        "2023-10-27",
        "2024-01-01",
        "2025-12-31",
        "2023/10/27",
        "not-a-date",
        "2023-13-01",
        12345
    ]
    for date_str in dates_to_test:
        result = formatter.format_date(date_str)
        print(f"Input: {date_str}, Output: {result}")