import datetime

class DateHelper:
    @staticmethod
    def get_day_of_week(date_string):
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return date_obj.strftime('%A')

if __name__ == '__main__':
    sample_date = '2023-10-05'
    day_of_week = DateHelper.get_day_of_week(sample_date)
    print(day_of_week)