import calendar

class WeekdayFinder:
    WEEKDAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    @staticmethod
    def get_weekday_name(year, month, day):
        date_obj = calendar.date(year, month, day)
        weekday_index = date_obj.weekday()
        return WeekdayFinder.WEEKDAY_NAMES[weekday_index]

if __name__ == '__main__':
    finder = WeekdayFinder()
    print(finder.get_weekday_name(2023, 10, 26))
    print(finder.get_weekday_name(2024, 1, 1))
    print(finder.get_weekday_name(2025, 12, 31))