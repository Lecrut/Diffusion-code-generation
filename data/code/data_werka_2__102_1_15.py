import calendar

class DateChecker:
    WEEKDAY_LIMIT = 5

    @staticmethod
    def parse_date(date_str):
        parts = date_str.split("-")
        return int(parts[0]), int(parts[1]), int(parts[2])

    @staticmethod
    def is_weekday(date_str):
        year, month, day = DateChecker.parse_date(date_str)
        weekday_index = calendar.weekday(year, month, day)
        return weekday_index < DateChecker.WEEKDAY_LIMIT

if __name__ == "__main__":
    test_dates = ["2023-10-01", "2023-10-02", "2023-10-07"]
    for date in test_dates:
        result = DateChecker.is_weekday(date)
        print(result)