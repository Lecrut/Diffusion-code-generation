import calendar

class WeekdayFinder:
    WEEKDAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    @staticmethod
    def get_weekday_name(year, month, day):
        return WeekdayFinder.WEEKDAY_NAMES[calendar.weekday(year, month, day)]

if __name__ == '__main__':
    print(WeekdayFinder.get_weekday_name(2023, 10, 26))
    print(WeekdayFinder.get_weekday_name(2024, 1, 1))
    print(WeekdayFinder.get_weekday_name(2025, 12, 31))