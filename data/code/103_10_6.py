import datetime

class TimeElapsedCalculator:
    TODAY = datetime.date(2023, 4, 1)

    @staticmethod
    def calculate_elapsed_time():
        now = datetime.datetime.now()
        midnight = datetime.datetime.combine(TimeElapsedCalculator.TODAY, datetime.time.min)
        elapsed_time = now - midnight
        return elapsed_time

if __name__ == '__main__':
    print(TimeElapsedCalculator.calculate_elapsed_time())