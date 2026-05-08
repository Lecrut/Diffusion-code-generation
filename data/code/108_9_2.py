import datetime
class DateUtils:
    @staticmethod
    def get_day_of_month(date_tuple):
        return date_tuple[1]
if __name__ == '__main__':
    sample_date = (2023, 10, 27)
    day = DateUtils.get_day_of_month(sample_date)
    print(day)