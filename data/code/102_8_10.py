from datetime import datetime

class DateChecker:

    def __init__(self):
        self.day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    def is_weekday(self, date_str):
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            day_index = date_obj.weekday()
            return day_index < 5
        except ValueError:
            raise ValueError('Invalid ISO format date string')
if __name__ == '__main__':
    checker = DateChecker()
    print(checker.is_weekday('2023-10-25'))
    print(checker.is_weekday('2023-10-28'))
    print(checker.is_weekday('2023-10-29'))