import datetime
class DateUtils:
    @classmethod
    def get_day_of_month(cls, date_tuple):
        day = date_tuple[1]
        return day
if __name__ == '__main__':
    sample_date = (2023, 10, 27)
    day = DateUtils.get_day_of_month(sample_date)
    print(day)