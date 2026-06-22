class TimeCalculator:
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60

    @staticmethod
    def time_difference(time1: int, time2: int) -> tuple:
        seconds_diff = abs(time2 - time1)
        hours = seconds_diff // (TimeCalculator.SECONDS_PER_MINUTE * TimeCalculator.MINUTES_PER_HOUR)
        minutes = (seconds_diff % (TimeCalculator.SECONDS_PER_MINUTE * TimeCalculator.MINUTES_PER_HOUR)) // TimeCalculator.SECONDS_PER_MINUTE
        seconds = seconds_diff % TimeCalculator.SECONDS_PER_MINUTE
        return hours, minutes, seconds

if __name__ == '__main__':
    result = TimeCalculator.time_difference(3600, 5400)
    print(result)