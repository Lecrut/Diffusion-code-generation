import time

class DayTimeCalculator:
    SECONDS_PER_HOUR = 3600
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    SECONDS_PER_DAY = HOURS_PER_DAY * SECONDS_PER_HOUR

    @staticmethod
    def get_seconds_in_hour():
        return DayTimeCalculator.SECONDS_PER_HOUR

    @staticmethod
    def get_total_seconds_in_day():
        return DayTimeCalculator.SECONDS_PER_DAY

    def calculate_fraction(self):
        now = time.localtime()
        hours = now.tm_hour
        minutes = now.tm_min
        seconds = now.tm_sec
        total_elapsed = (hours * self.get_seconds_in_hour()) + (minutes * self.MINUTES_PER_HOUR) + seconds
        return total_elapsed / self.get_total_seconds_in_day()

if __name__ == '__main__':
    calculator = DayTimeCalculator()
    result = calculator.calculate_fraction()
    print(result)