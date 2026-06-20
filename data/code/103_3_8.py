import datetime

class TimeTracker:
    def total_seconds_elapsed_today(self):
        now = datetime.datetime.now()
        start_of_day = datetime.datetime(now.year, now.month, now.day)
        return (now - start_of_day).total_seconds()

if __name__ == '__main__':
    tracker = TimeTracker()
    print(tracker.total_seconds_elapsed_today())