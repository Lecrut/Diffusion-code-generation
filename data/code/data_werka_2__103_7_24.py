from datetime import datetime, timedelta

class DayProgress:
    def __init__(self, now=None):
        self.now = now if now is not None else datetime.now()
        self.start_of_day = datetime.min.replace(year=self.now.year, month=self.now.month, day=self.now.day)
        self.elapsed = self.now - self.start_of_day
        self.total_seconds = self.elapsed.total_seconds()
        self.hours = int(self.total_seconds // 3600)
        self.minutes = int((self.total_seconds % 3600) // 60)
        self.seconds = int(self.total_seconds % 60)

    def get_elapsed(self):
        return self.elapsed

    def get_formatted(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def get_total_seconds(self):
        return self.total_seconds

if __name__ == '__main__':
    progress = DayProgress()
    print(progress.get_elapsed())
    print(progress.get_formatted())
    print(progress.get_total_seconds())