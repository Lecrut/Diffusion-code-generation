import time

class DateChecker:
    WEEKDAY_THRESHOLD = 5

    @staticmethod
    def get_current_weekday_index():
        return time.localtime().tm_wday

    @staticmethod
    def is_weekday():
        return DateChecker.get_current_weekday_index() < DateChecker.WEEKDAY_THRESHOLD

if __name__ == '__main__':
    checker = DateChecker()
    print(checker.is_weekday())