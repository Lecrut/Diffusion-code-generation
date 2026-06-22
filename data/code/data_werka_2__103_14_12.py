import datetime

class TimeTracker:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def get_elapsed_seconds(self):
        delta = self.end_time - self.start_time
        return int(delta.total_seconds())

    def format_elapsed(self):
        total = self.get_elapsed_seconds()
        hours, remainder = divmod(total, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    sample_start = datetime.datetime(2023, 10, 1, 8, 30, 0)
    sample_end = datetime.datetime(2023, 10, 1, 14, 45, 20)
    tracker = TimeTracker(sample_start, sample_end)
    print(tracker.format_elapsed())