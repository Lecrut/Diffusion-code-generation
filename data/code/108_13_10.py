from datetime import date

class DateHandler:
    def __init__(self, year, month, day):
        self.date_obj = date(year, month, day)
    
    def get_day_of_month(self):
        return self.date_obj.day

if __name__ == '__main__':
    handler = DateHandler(2024, 10, 10)
    print(handler.get_day_of_month())