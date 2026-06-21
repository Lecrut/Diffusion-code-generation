import datetime
import time

class TimeElapsedTracker:
    def __init__(self, reference_dt):
        self.reference_dt = reference_dt
        self.epoch = datetime.datetime(1970, 1, 1)
        self.seconds_per_day = 86400

    def get_elapsed_seconds(self):
        start_of_day = self.reference_dt.replace(hour=0, minute=0, second=0, microsecond=0)
        delta = self.reference_dt - start_of_day
        return delta.total_seconds()

    def get_fractional_day(self):
        elapsed = self.get_elapsed_seconds()
        return elapsed / self.seconds_per_day

    def get_microseconds_elapsed(self):
        start_of_day = self.reference_dt.replace(hour=0, minute=0, second=0, microsecond=0)
        delta = self.reference_dt - start_of_day
        return int(delta.total_seconds() * 1000000)

if __name__ == '__main__':
    sample_dt = datetime.datetime(2023, 11, 15, 14, 30, 15, 500000)
    tracker = TimeElapsedTracker(sample_dt)
    elapsed_sec = tracker.get_elapsed_seconds()
    frac_day = tracker.get_fractional_day()
    micro_sec = tracker.get_microseconds_elapsed()
    print(elapsed_sec)
    print(frac_day)
    print(micro_sec)