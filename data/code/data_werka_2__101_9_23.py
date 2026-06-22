import datetime

class DayOfWeekResolver:
    def __init__(self, date_string):
        self.date_string = date_string

    def parse_date(self):
        return datetime.datetime.strptime(self.date_string, "%Y-%m-%d")

    def get_day_name_upper(self):
        dt = self.parse_date()
        return dt.strftime("%A").upper()

    def get_day_index(self):
        dt = self.parse_date()
        return dt.weekday()

if __name__ == '__main__':
    date_input = "2023-11-11"
    resolver = DayOfWeekResolver(date_input)
    print(resolver.get_day_name_upper())
    print(resolver.get_day_index())