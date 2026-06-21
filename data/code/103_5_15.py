import threading
from datetime import datetime, time as dt_time

class TimeCalculator:
    def __init__(self):
        self._lock = threading.Lock()

    def _validate_time(self, t: dt_time) -> dt_time:
        if t is None:
            raise ValueError("Time object cannot be None")
        if not isinstance(t, dt_time):
            raise TypeError("Input must be a time object")
        return t

    def calculate_elapsed_seconds(self, reference_time: datetime | None = None) -> float:
        if reference_time is None:
            reference_time = datetime.now()
        
        with self._lock:
            validated_time = self._validate_time(reference_time.time())
            midnight = dt_time.min
            validated_midnight = self._validate_time(midnight)
            
            if validated_time < validated_midnight:
                raise ValueError("Time cannot be before midnight")
            
            seconds = (
                validated_time.hour * 3600
                + validated_time.minute * 60
                + validated_time.second
                + validated_time.microsecond / 1_000_000
            )
            return seconds

def main() -> None:
    calculator = TimeCalculator()
    sample_time = datetime(2023, 10, 1, 12, 30, 45, 123456)
    result = calculator.calculate_elapsed_seconds(sample_time)
    print(result)

if __name__ == '__main__':
    main()