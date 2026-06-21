import datetime
import time

class DayTimer:
    def __init__(self, reference_time=None):
        if reference_time is None:
            self.reference_time = datetime.datetime.now()
        else:
            if not isinstance(reference_time, datetime.datetime):
                raise ValueError("reference_time must be a datetime object")
            self.reference_time = reference_time

    def get_elapsed_time(self):
        now = self.reference_time
        start_of_day = datetime.datetime.min.replace(year=now.year, month=now.month, day=now.day)
        elapsed = now - start_of_day
        return elapsed

    def get_formatted_elapsed(self):
        elapsed = self.get_elapsed_time()
        total_seconds = int(elapsed.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    timer = DayTimer()
    print(timer.get_formatted_elapsed())