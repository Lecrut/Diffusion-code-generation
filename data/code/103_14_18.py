import datetime

class TimeTracker:
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    def __init__(self, reference_time=None):
        if reference_time is None:
            self.reference_time = datetime.datetime.now()
        else:
            self.reference_time = reference_time

    def get_elapsed_seconds(self):
        start_of_day = self.reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
        delta = self.reference_time - start_of_day
        return int(delta.total_seconds())

    def format_elapsed(self):
        total_seconds = self.get_elapsed_seconds()
        hours, remainder = divmod(total_seconds, TimeTracker.SECONDS_PER_HOUR)
        minutes, seconds = divmod(remainder, TimeTracker.SECONDS_PER_MINUTE)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    tracker = TimeTracker()
    print(tracker.format_elapsed())