import datetime

class TimeCalculator:
    def __init__(self):
        self.now = datetime.datetime.now()

    def calculate_fractional_day(self):
        fractional_day = (self.now - datetime.datetime.combine(self.now.date(), datetime.time.min)).total_seconds()
        return fractional_day

if __name__ == '__main__':
    calculator = TimeCalculator()
    fractional_day = calculator.calculate_fractional_day()
    print(fractional_day)