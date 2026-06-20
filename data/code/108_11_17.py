import datetime

class DateProcessor:
    def __init__(self, year, month, day):
        self.date_obj = datetime.date(year, month, day)

    def get_day_of_month(self):
        return self.date_obj.day

if __name__ == '__main__':
    processor = DateProcessor(2023, 3, 15)
    print(processor.get_day_of_month())