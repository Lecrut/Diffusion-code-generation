from datetime import datetime, timedelta

class TimeTracker:
    def __init__(self):
        self.now = datetime.now()

    @property
    def total_seconds_elapsed_today(self):
        start_of_day = datetime(self.now.year, self.now.month, self.now.day)
        return (self.now - start_of_day).total_seconds()

if __name__ == '__main__':
    tracker = TimeTracker()
    print(tracker.total_seconds_elapsed_today)