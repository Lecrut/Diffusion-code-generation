import datetime

class DateUtils:
    @staticmethod
    def first_day_of_next_month(date_str):
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        next_month = (date_obj.replace(day=28) + datetime.timedelta(days=4)).replace(day=1)
        return next_month.strftime('%Y-%m-%d')

if __name__ == '__main__':
    sample_date_str = "2023-10-15"
    date_utils = DateUtils()
    print(date_utils.first_day_of_next_month(sample_date_str))