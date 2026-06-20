from datetime import datetime

class TimeTracker:
    def __init__(self):
        self.now = datetime.now()
    
    @staticmethod
    def get_start_of_day(dt):
        return dt.replace(hour=0, minute=0, second=0, microsecond=0)
    
    @property
    def total_seconds_elapsed_today(self):
        start_of_day = TimeTracker.get_start_of_day(self.now)
        return (self.now - start_of_day).total_seconds()

if __name__ == '__main__':
    tracker = TimeTracker()
    print(tracker.total_seconds_elapsed_today)