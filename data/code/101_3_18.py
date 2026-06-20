import datetime

class DateProcessor:
    WEEKDAY_NAMES = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    ]

    @staticmethod
    def get_day_of_week(date_string):
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        weekday_index = date_obj.weekday()
        return DateProcessor.WEEKDAY_NAMES[weekday_index]

if __name__ == '__main__':
    sample_date = '2023-12-25'
    day_name = DateProcessor.get_day_of_week(sample_date)
    print(day_name)