import datetime
import time

def get_fractional_day_passed() -> float:
    now = datetime.datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - start_of_day
    total_seconds = delta.total_seconds()
    fractional_day = total_seconds / 86400.0
    return fractional_day

def fractional_day_to_seconds(fractional_day: float) -> float:
    if not (0.0 <= fractional_day <= 1.0):
        raise ValueError("Fractional day must be between 0.0 and 1.0")
    return fractional_day * 86400.0

if __name__ == '__main__':
    frac = get_fractional_day_passed()
    seconds = fractional_day_to_seconds(frac)
    print(seconds)