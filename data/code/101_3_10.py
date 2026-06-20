import datetime

class DateHelper:
    WEEKDAY_NAMES = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    @staticmethod
    def get_day_of_week(date_string):
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        weekday_index = date_obj.weekday()
        return DateHelper.WEEKDAY_NAMES[weekday_index]

if __name__ == '__main__':
    day_name = DateHelper.get_day_of_week('2023-12-25')
    print(day_name)