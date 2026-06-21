class DateProcessor:
    DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def get_days_in_month(year, month):
        if month == 2:
            return 29 if DateProcessor.is_leap_year(year) else 28
        return DateProcessor.DAYS_IN_MONTH[month - 1]

    @staticmethod
    def validate_date(year, month, day):
        if not (1 <= month <= 12):
            raise ValueError(f"Invalid month: {month}")
        max_days = DateProcessor.get_days_in_month(year, month)
        if not (1 <= day <= max_days):
            raise ValueError(f"Invalid day: {day} for month {month} in year {year}")
        return True

    @staticmethod
    def extract_day(date_str):
        parts = date_str.split("-")
        if len(parts) != 3:
            raise ValueError(f"Invalid date format: {date_str}")
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        DateProcessor.validate_date(year, month, day)
        return day

if __name__ == '__main__':
    sample_dates = ["2023-10-05", "2024-02-29", "2025-12-31"]
    for date_str in sample_dates:
        day = DateProcessor.extract_day(date_str)
        print(day)