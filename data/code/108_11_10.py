import datetime

class DateHandler:
    def __init__(self, year=2023, month=3, day=15):
        self.date_obj = datetime.date(year, month, day)
    
    def get_day_of_month(self):
        return self.date_obj.day

if __name__ == '__main__':
    handler = DateHandler()
    print(f"Day of month: {handler.get_day_of_month()}")