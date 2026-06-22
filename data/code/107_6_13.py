from datetime import datetime

class DateFormatter:
    def __init__(self, year, month, day):
        self.date_obj = datetime(year, month, day)

    def format(self):
        day_name = self.date_obj.strftime('%A')
        month_name = self.date_obj.strftime('%B')
        day = self.date_obj.day
        year = self.date_obj.year
        return f"{day_name}, {month_name} {day:02d}, {year}"

    def get_raw_date(self):
        return self.date_obj

if __name__ == '__main__':
    formatter = DateFormatter(2023, 10, 25)
    print(formatter.format())
    print(formatter.get_raw_date())
    formatter2 = DateFormatter(2000, 1, 1)
    print(formatter2.format())