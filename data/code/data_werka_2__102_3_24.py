class DateChecker:
    def __init__(self, reference_time=None):
        self.reference_time = reference_time

    def is_weekday(self):
        import time
        check_time = self.reference_time if self.reference_time else time.localtime()
        day_index = check_time.tm_wday
        return 0 <= day_index <= 4

    def is_weekend(self):
        import time
        check_time = self.reference_time if self.reference_time else time.localtime()
        day_index = check_time.tm_wday
        return not self.is_weekday()

    def get_day_name(self):
        import time
        check_time = self.reference_time if self.reference_time else time.localtime()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[check_time.tm_wday]

if __name__ == '__main__':
    checker = DateChecker()
    print(checker.is_weekday())
    print(checker.is_weekend())
    print(checker.get_day_name())