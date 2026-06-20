import datetime

class DateProcessor:
    def __init__(self, date_str):
        day, month, year = map(int, date_str.split('-'))
        self.date_obj = datetime.date(year, month, day)

    def get_weekday(self):
        return self.date_obj.strftime("%A").upper()

if __name__ == '__main__':
    sample_date = "04-07-2024"
    processor = DateProcessor(sample_date)
    print(processor.get_weekday())