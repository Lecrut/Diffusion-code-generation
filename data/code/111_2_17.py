import datetime

class DateHandler:
    def get_day_of_week(self, year, month, day):
        date = datetime.date(year, month, day)
        return date.strftime('%A')

if __name__ == '__main__':
    handler = DateHandler()
    print(handler.get_day_of_week(2024, 2, 29))