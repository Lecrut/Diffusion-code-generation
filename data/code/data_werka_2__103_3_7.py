from datetime import datetime, timedelta
class ElapsedTimeCalculator:
    def __init__(self, current_time=None):
        self.current_time = current_time if current_time else datetime.now()
        self.start_of_day = self.current_time.replace(hour=0, minute=0, second=0, microsecond=0)
    def get_elapsed_seconds(self):
        delta = self.current_time - self.start_of_day
        return int(delta.total_seconds())
if __name__ == '__main__':
    sample_time = datetime(2024, 1, 15, 14, 30, 0)
    calc = ElapsedTimeCalculator(sample_time)
    print(calc.get_elapsed_seconds())