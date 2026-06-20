from datetime import date

class DateProcessor:
    def __init__(self, year=2024, month=10, day=10):
        self.date_obj = date(year, month, day)

    def get_day_of_month(self):
        return self.date_obj.day

if __name__ == '__main__':
    processor = DateProcessor()
    print(processor.get_day_of_month())