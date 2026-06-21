import time

class TimeCalculator:
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_MINUTE = 60

    @staticmethod
    def calculate_seconds_since_midnight():
        current_timestamp = time.time()
        local_time = time.localtime(current_timestamp)
        hours = local_time.tm_hour
        minutes = local_time.tm_min
        seconds = local_time.tm_sec
        elapsed = (hours * TimeCalculator.SECONDS_IN_HOUR) + (minutes * TimeCalculator.SECONDS_IN_MINUTE) + seconds
        return elapsed

if __name__ == '__main__':
    calculator = TimeCalculator()
    result = calculator.calculate_seconds_since_midnight()
    print(result)