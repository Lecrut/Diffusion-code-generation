import datetime

SECONDS_IN_DAY = 86400

class MidnightTimer:
    seconds_per_hour = 3600
    minutes_per_hour = 60

    def __init__(self, reference_time=None):
        if reference_time is None:
            self.now = datetime.datetime.now()
        else:
            self.now = reference_time
        self.midnight = self.now.replace(hour=0, minute=0, second=0, microsecond=0)

    def calculate_elapsed_seconds(self):
        delta = self.now - self.midnight
        return delta.total_seconds()

    def get_hours_elapsed(self):
        seconds = self.calculate_elapsed_seconds()
        return seconds / self.seconds_per_hour

    def get_minutes_elapsed(self):
        seconds = self.calculate_elapsed_seconds()
        return seconds / self.minutes_per_hour

if __name__ == '__main__':
    timer = MidnightTimer()
    elapsed = timer.calculate_elapsed_seconds()
    print(elapsed)