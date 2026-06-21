import calendar

class WeekdayResolver:
    DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    @staticmethod
    def get_weekday_name(year, month, day):
        index = calendar.weekday(year, month, day)
        return WeekdayResolver.DAY_NAMES[index]

if __name__ == '__main__':
    resolver = WeekdayResolver()
    result = resolver.get_weekday_name(2024, 2, 29)
    print(result)