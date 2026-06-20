import datetime

class DateProcessor:
    @staticmethod
    def get_day_of_month(year, month, day):
        date_obj = datetime.date(year, month, day)
        return date_obj.day

if __name__ == '__main__':
    sample_date = (2023, 10, 26)
    print(DateProcessor.get_day_of_month(*sample_date))