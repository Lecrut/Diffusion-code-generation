import time

class DateCalculator:
    def get_day_of_month(self):
        current_time = time.localtime()
        return current_time.tm_mday

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.get_day_of_month())