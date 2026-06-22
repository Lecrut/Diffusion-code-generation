import datetime

class WeekdayResolver:
    def __init__(self, year, month, day):
        self.date_obj = datetime.date(year, month, day)

    def get_weekday_name(self):
        return self.date_obj.strftime('%A').upper()

    def get_iso_weekday_number(self):
        return self.date_obj.isoweekday()

if __name__ == '__main__':
    resolver = WeekdayResolver(2024, 7, 4)
    print(resolver.get_weekday_name())
    print(resolver.get_iso_weekday_number())