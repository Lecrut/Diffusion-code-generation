import calendar

class DateFormatter:
    MONTH_NAMES = calendar.month_name

    @staticmethod
    def _validate_date_parts(parts):
        if len(parts) != 3:
            raise ValueError("Date string must contain exactly three parts separated by hyphens")
        try:
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
        except ValueError:
            raise ValueError("Date parts must be integers")
        if not (1 <= month <= 12):
            raise ValueError(f"Invalid month: {month}")
        if not (1 <= day <= 31):
            raise ValueError(f"Invalid day: {day}")
        if year < 1:
            raise ValueError(f"Invalid year: {year}")
        return year, month, day

    @staticmethod
    def format_date(date_str):
        parts = date_str.split('-')
        year, month, day = DateFormatter._validate_date_parts(parts)
        month_name = DateFormatter.MONTH_NAMES[month]
        return f"{month_name} {day:02d}, {year}"

if __name__ == '__main__':
    sample_dates = ['2023-1-5', '2024-12-25', '2000-2-29']
    for date_str in sample_dates:
        result = DateFormatter.format_date(date_str)
        print(result)