import datetime
import math

class DailyElapsedTimer:
    def __init__(self, reference_now=None):
        if reference_now is None:
            self.reference_now = datetime.datetime.now()
        elif not isinstance(reference_now, datetime.datetime):
            raise ValueError("reference_now must be a datetime object")
        else:
            self.reference_now = reference_now
        self.start_of_day = datetime.datetime.min.replace(
            year=self.reference_now.year,
            month=self.reference_now.month,
            day=self.reference_now.day
        )

    def get_elapsed_delta(self):
        return self.reference_now - self.start_of_day

    def get_total_seconds(self):
        delta = self.get_elapsed_delta()
        return delta.total_seconds()

    def get_hours(self):
        return math.floor(self.get_total_seconds() / 3600)

    def get_minutes(self):
        return math.floor((self.get_total_seconds() % 3600) / 60)

    def get_seconds(self):
        return math.floor(self.get_total_seconds() % 60)

if __name__ == '__main__':
    timer = DailyElapsedTimer()
    delta = timer.get_elapsed_delta()
    total_secs = timer.get_total_seconds()
    hours = timer.get_hours()
    minutes = timer.get_minutes()
    seconds = timer.get_seconds()
    print(delta)
    print(total_secs)
    print(hours)
    print(minutes)
    print(seconds)