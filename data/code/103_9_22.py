from datetime import datetime, time

class TimeCalculator:
    def __init__(self, reference_time: datetime = None):
        self.reference_time = reference_time if reference_time else datetime.now()

    def get_elapsed_since_midnight(self) -> str:
        midnight = datetime.combine(self.reference_time.date(), time.min)
        delta = self.reference_time - midnight
        total_seconds = int(delta.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def get_reference_time(self) -> datetime:
        return self.reference_time

if __name__ == '__main__':
    calc = TimeCalculator(datetime(2023, 10, 27, 14, 30, 45))
    print(calc.get_elapsed_since_midnight())
    print(calc.get_reference_time())