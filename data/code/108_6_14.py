import datetime

class DateHandler:
    def __init__(self, dates):
        self.dates = dates

    def get_day_of_month(self, date_str):
        year, month, day = map(int, date_str.split('-'))
        return datetime.date(year, month, day).day

if __name__ == '__main__':
    sample_dates = ['2023-10-05', '2023-11-15', '2024-02-29']
    date_handler = DateHandler(sample_dates)
    for date in date_handler.dates:
        print(date_handler.get_day_of_month(date))