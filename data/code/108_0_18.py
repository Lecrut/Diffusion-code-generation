import datetime

class DateHandler:
    def __init__(self, year, month, day):
        self.date = datetime.date(year, month, day)

    def get_day_of_month(self):
        return self.date.day

if __name__ == '__main__':
    handler = DateHandler(2023, 10, 26)
    print(handler.get_day_of_month())