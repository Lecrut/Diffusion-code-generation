from datetime import datetime

class TimeSinceMidnight:
    def __init__(self):
        now = datetime.now()
        self.midnight = datetime(now.year, now.month, now.day)

    def get_elapsed_seconds(self):
        now = datetime.now()
        elapsed_time = now - self.midnight
        return elapsed_time.total_seconds()

if __name__ == '__main__':
    time_calculator = TimeSinceMidnight()
    print(time_calculator.get_elapsed_seconds())