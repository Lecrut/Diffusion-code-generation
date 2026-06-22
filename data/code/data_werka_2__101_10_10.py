import calendar

class DateAnalyzer:
    DAY_NAMES = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    )

    @staticmethod
    def get_weekday_name(year: int, month: int, day: int) -> str:
        weekday_index = calendar.weekday(year, month, day)
        return DateAnalyzer.DAY_NAMES[weekday_index]

if __name__ == '__main__':
    year = 2023
    month = 12
    day = 25
    analyzer = DateAnalyzer()
    result = analyzer.get_weekday_name(year, month, day)
    print(result)