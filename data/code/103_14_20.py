import datetime

class TimeElapsedCalculator:
    def __init__(self, reference_time=None):
        if reference_time is None:
            self.reference_time = datetime.datetime.now()
        else:
            self.reference_time = reference_time

    def get_elapsed_since_midnight(self):
        midnight = self.reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
        delta = self.reference_time - midnight
        total_seconds = int(delta.total_seconds())
        
        hours = total_seconds // 3600
        remaining_seconds = total_seconds % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    sample_time = datetime.datetime(2023, 10, 5, 14, 30, 45)
    calculator = TimeElapsedCalculator(sample_time)
    result = calculator.get_elapsed_since_midnight()
    print(result)