class DateFormatter:
    def format_date(self, date_string):
        try:
            if not isinstance(date_string, str):
                raise ValueError("Input must be a string.")
            parts = date_string.split('-')
            if len(parts) != 3:
                raise ValueError("Date string format incorrect. Expected YYYY-MM-DD.")
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError("Invalid month or day values.")
            formatted_date = f"{year}{month:02d}{day:02d}"
            return int(formatted_date)
        except ValueError:
            return None
        except Exception:
            return None
if __name__ == '__main__':
    formatter = DateFormatter()
    sample_dates = [
        "2023-10-27",
        "1999-01-01",
        "2024-02-29",
        "2023/10/27",
        "not-a-date",
        12345
    ]
    for date_str in sample_dates:
        result = formatter.format_date(date_str)
        print(f"Input: {date_str}, Output: {result}")