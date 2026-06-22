import datetime
import time

class TimeDeltaCalculator:
    def __init__(self, reference_time: datetime.datetime = None):
        self.reference_time = reference_time if reference_time is not None else datetime.datetime.now()

    def get_seconds_since_midnight(self) -> float:
        start_of_day = self.reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
        delta = self.reference_time - start_of_day
        return delta.total_seconds()

    def get_current_timestamp(self) -> int:
        return int(time.time())

    def format_elapsed_time(self) -> str:
        total_seconds = int(self.get_seconds_since_midnight())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    calculator = TimeDeltaCalculator()
    elapsed_seconds = calculator.get_seconds_since_midnight()
    current_ts = calculator.get_current_timestamp()
    formatted_time = calculator.format_elapsed_time()
    print(elapsed_seconds)
    print(current_ts)
    print(formatted_time)