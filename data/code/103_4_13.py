import datetime

class TimeCalculator:
    def __init__(self):
        self.now = datetime.datetime.now()

    def get_fractional_day(self):
        return (self.now - datetime.datetime.combine(self.now.date(), datetime.time.min)).total_seconds()

if __name__ == '__main__':
    calculator = TimeCalculator()
    fractional_day_seconds = calculator.get_fractional_day()
    print(fractional_day_seconds)