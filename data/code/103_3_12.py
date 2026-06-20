from datetime import datetime

class TimeCalculator:
    @staticmethod
    def total_seconds_elapsed_today():
        now = datetime.now()
        start_of_day = datetime(now.year, now.month, now.day)
        return (now - start_of_day).total_seconds()

if __name__ == '__main__':
    print(TimeCalculator.total_seconds_elapsed_today())