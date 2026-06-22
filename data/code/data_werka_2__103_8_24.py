import time

class TimeElapsedCalculator:
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    @staticmethod
    def get_elapsed_seconds_today() -> int:
        current_struct_time = time.localtime()
        hours = current_struct_time.tm_hour
        minutes = current_struct_time.tm_min
        seconds = current_struct_time.tm_sec
        total = hours * TimeElapsedCalculator.SECONDS_PER_HOUR
        total += minutes * TimeElapsedCalculator.SECONDS_PER_MINUTE
        total += seconds
        return total

if __name__ == '__main__':
    calculator = TimeElapsedCalculator()
    result = calculator.get_elapsed_seconds_today()
    print(result)