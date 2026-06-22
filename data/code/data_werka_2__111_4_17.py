class YearTimeCalculator:
    def __init__(self, days=365):
        self.days = days
        self.hours_per_day = 24
        self.minutes_per_hour = 60
        self.seconds_per_minute = 60

    def calculate_seconds(self):
        return self.days * self.hours_per_day * self.minutes_per_hour * self.seconds_per_minute

    def get_days(self):
        return self.days

if __name__ == '__main__':
    calc = YearTimeCalculator()
    print(calc.calculate_seconds())
    print(calc.get_days())