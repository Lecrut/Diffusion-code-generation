import time

class TimeCalculator:
    DAY_OF_MONTH_INDEX = 3

    @staticmethod
    def get_structured_time():
        return time.localtime()

    def get_current_day(self):
        local_time = self.get_structured_time()
        return local_time[self.DAY_OF_MONTH_INDEX]

if __name__ == '__main__':
    calculator = TimeCalculator()
    day = calculator.get_current_day()
    print(day)
    sample_time = time.mktime((2023, 10, 15, 12, 0, 0, 0, 0, 0))
    sample_structured = time.localtime(sample_time)
    sample_day = sample_structured[TimeCalculator.DAY_OF_MONTH_INDEX]
    print(sample_day)