from datetime import datetime, timedelta

class DayElapsedCounter:
    def __init__(self, reference_time=None):
        self.reference_time = reference_time if reference_time else datetime.now()
        self.day_start = self.reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
    
    def get_elapsed_seconds(self):
        delta = self.reference_time - self.day_start
        return int(delta.total_seconds())

if __name__ == '__main__':
    sample_time = datetime(2024, 6, 15, 9, 45, 30)
    counter = DayElapsedCounter(sample_time)
    print(counter.get_elapsed_seconds())