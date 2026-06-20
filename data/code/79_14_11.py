import datetime

class DateHandler:
    def __init__(self, year=2024, month=3, day=31):
        self.date_obj = datetime.datetime(year, month, day)

    def get_next_month_date(self):
        next_month = self.date_obj.replace(day=1) + datetime.timedelta(days=31)
        return next_month.strftime('%Y-%m-%d')

if __name__ == '__main__':
    handler = DateHandler()
    print(handler.get_next_month_date())