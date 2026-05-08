import datetime
class TimeTracker:
    def get_time_elapsed_today(self):
        now = datetime.datetime.now()
        start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
        elapsed_time = now - start_of_day
        return elapsed_time
if __name__ == '__main__':
    tracker = TimeTracker()
    elapsed = tracker.get_time_elapsed_today()
    print(elapsed)