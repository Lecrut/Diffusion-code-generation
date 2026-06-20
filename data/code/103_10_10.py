import datetime

class TimeSinceMidnight:
    @staticmethod
    def calculate():
        today = datetime.datetime(2023, 4, 1)
        now = datetime.datetime.now()
        midnight = today.replace(hour=0, minute=0, second=0, microsecond=0)
        elapsed_time = now - midnight
        return elapsed_time

if __name__ == '__main__':
    result = TimeSinceMidnight.calculate()
    print(result)