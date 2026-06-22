import time

class DateChecker:
    def __init__(self):
        self.weekday_limit = 5

    def is_weekday(self):
        current_time = time.localtime()
        return current_time.tm_wday < self.weekday_limit

    def get_current_day_name(self):
        day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        current_time = time.localtime()
        return day_names[current_time.tm_wday]

if __name__ == '__main__':
    checker = DateChecker()
    print(checker.is_weekday())
    print(checker.get_current_day_name())