import datetime

class DateProcessor:
    def get_weekday(self, date_str):
        day, month, year = map(int, date_str.split('-'))
        date_obj = datetime.date(year, month, day)
        return date_obj.strftime("%A").upper()

if __name__ == '__main__':
    processor = DateProcessor()
    sample_date = "04-07-2024"
    print(processor.get_weekday(sample_date))