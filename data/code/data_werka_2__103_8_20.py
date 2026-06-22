import time

class TimeCalculator:
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    @staticmethod
    def get_current_time_struct():
        return time.localtime()

    @classmethod
    def calculate_elapsed_seconds_today(cls):
        current_time = cls.get_current_time_struct()
        hours = current_time.tm_hour
        minutes = current_time.tm_min
        seconds = current_time.tm_sec
        return hours * cls.SECONDS_PER_HOUR + minutes * cls.SECONDS_PER_MINUTE + seconds

if __name__ == '__main__':
    calculator = TimeCalculator()
    elapsed = calculator.calculate_elapsed_seconds_today()
    print(elapsed)