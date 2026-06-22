from datetime import timedelta

class YearCalculator:
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    DAYS_IN_NON_LEAP_YEAR = 365

    @staticmethod
    def calculate_seconds():
        seconds_per_day = YearCalculator.SECONDS_PER_MINUTE * YearCalculator.MINUTES_PER_HOUR * YearCalculator.HOURS_PER_DAY
        total_seconds = YearCalculator.DAYS_IN_NON_LEAP_YEAR * seconds_per_day
        return total_seconds

if __name__ == '__main__':
    calc = YearCalculator()
    result = calc.calculate_seconds()
    print(result)