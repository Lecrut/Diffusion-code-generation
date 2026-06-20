import datetime

class TimeElapsedCalculator:
    MIDNIGHT = datetime.time(0, 0, 0)

    @staticmethod
    def calculate_time_elapsed():
        now = datetime.datetime.now()
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
        return now - midnight

if __name__ == '__main__':
    elapsed_time = TimeElapsedCalculator.calculate_time_elapsed()
    print(elapsed_time)