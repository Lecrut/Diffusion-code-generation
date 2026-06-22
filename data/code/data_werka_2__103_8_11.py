import time

class TimeCalculator:
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    @staticmethod
    def get_elapsed_seconds_today() -> int:
        current = time.localtime()
        hours = current.tm_hour
        minutes = current.tm_min
        seconds = current.tm_sec
        return (hours * TimeCalculator.SECONDS_PER_HOUR) + (minutes * TimeCalculator.SECONDS_PER_MINUTE) + seconds

if __name__ == '__main__':
    calculator = TimeCalculator()
    elapsed = calculator.get_elapsed_seconds_today()
    print(elapsed)