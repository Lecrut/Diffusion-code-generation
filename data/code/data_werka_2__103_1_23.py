class TimeElapsedCalculator:
    SECONDS_PER_MINUTE = 60
    MILLISECONDS_PER_SECOND = 1000
    MILLISECONDS_PER_MINUTE = SECONDS_PER_MINUTE * MILLISECONDS_PER_SECOND
    MILLISECONDS_PER_HOUR = MILLISECONDS_PER_MINUTE * 60

    @staticmethod
    def calculate() -> int:
        import time
        now = time.localtime()
        hours = now.tm_hour
        minutes = now.tm_min
        seconds = now.tm_sec
        millis = now.tm_msec
        total = (hours * TimeElapsedCalculator.MILLISECONDS_PER_HOUR) + (minutes * TimeElapsedCalculator.MILLISECONDS_PER_MINUTE) + (seconds * TimeElapsedCalculator.MILLISECONDS_PER_SECOND) + millis
        return total

if __name__ == '__main__':
    calculator = TimeElapsedCalculator()
    result = calculator.calculate()
    print(result)