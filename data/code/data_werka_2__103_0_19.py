import datetime

class MidnightTimer:
    def __init__(self):
        self.reference = datetime.datetime.now()
        self.midnight = self.reference.replace(hour=0, minute=0, second=0, microsecond=0)
        self.elapsed_seconds = (self.reference - self.midnight).total_seconds()

    def get_seconds(self):
        return self.elapsed_seconds

    def get_hours(self):
        return self.elapsed_seconds / 3600

    def get_minutes(self):
        return self.elapsed_seconds / 60

if __name__ == '__main__':
    timer = MidnightTimer()
    print(timer.get_seconds())
    print(timer.get_hours())
    print(timer.get_minutes())