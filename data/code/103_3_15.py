from datetime import datetime

def seconds_elapsed_today():
    now = datetime.now()
    start_of_day = datetime(now.year, now.month, now.day)
    return (now - start_of_day).total_seconds()

if __name__ == '__main__':
    sample_time = datetime(2023, 10, 28, 9, 45, 0)
    time_tracker = TimeTracker()
    print(time_tracker.total_seconds_elapsed(sample_time))
    
class TimeTracker:
    @staticmethod
    def total_seconds_elapsed(time):
        start_of_day = datetime(time.year, time.month, time.day)
        return (time - start_of_day).total_seconds()