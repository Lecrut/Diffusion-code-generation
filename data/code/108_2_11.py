import time

class DateExtractor:
    def __init__(self):
        self.current_time = None
        self.day_of_month = 0

    def update_current_time(self):
        self.current_time = time.localtime()

    def get_day_of_month(self):
        if not self.current_time:
            self.update_current_time()
        self.day_of_month = self.current_time.tm_mday
        return self.day_of_month

if __name__ == '__main__':
    calculator = DateExtractor()
    day = calculator.get_day_of_month()
    print(day)