import time

class TimeCalculator:
    DAY_OF_MONTH_INDEX = 3

    @staticmethod
    def get_current_day_of_month():
        now = time.localtime()
        return now[TimeCalculator.DAY_OF_MONTH_INDEX]

if __name__ == '__main__':
    calculator = TimeCalculator()
    day = calculator.get_current_day_of_month()
    print(day)