import datetime

class DateProcessor:
    def __init__(self, year, month, day):
        self.date = datetime.date(year, month, day)

    def get_day_of_week(self):
        return self.date.strftime('%A')

if __name__ == '__main__':
    processor = DateProcessor(2024, 2, 29)
    print(f"Day of the week for February 29, 2024: {processor.get_day_of_week()}")