import datetime

class DateHandler:
    def __init__(self, base_date):
        self.base_date = base_date

    def nearest_saturday(self):
        days_until_saturday = (5 - self.base_date.weekday()) % 7
        return self.base_date + datetime.timedelta(days=days_until_saturday)

if __name__ == '__main__':
    handler = DateHandler(datetime.date(2023, 11, 1))
    nearest_sat = handler.nearest_saturday()
    print(f"Nearest upcoming Saturday: {nearest_sat}")