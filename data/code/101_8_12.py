import calendar

class WeekdayResolver:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_full_weekday_name(self):
        index = calendar.weekday(self.year, self.month, self.day)
        return calendar.day_name[index]

if __name__ == '__main__':
    resolver = WeekdayResolver(2024, 1, 1)
    print(resolver.get_full_weekday_name())
    resolver_2 = WeekdayResolver(2020, 2, 29)
    print(resolver_2.get_full_weekday_name())