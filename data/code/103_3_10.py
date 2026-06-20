import datetime

class TimeCalculator:
    @staticmethod
    def get_seconds_elapsed_today():
        now = datetime.datetime.now()
        start_of_day = datetime.datetime(now.year, now.month, now.day)
        return (now - start_of_day).total_seconds()

if __name__ == '__main__':
    print(TimeCalculator.get_seconds_elapsed_today())