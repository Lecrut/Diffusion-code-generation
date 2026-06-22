from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

SECONDS_PER_HOUR = 3600

def calculate_duration_hours(start_dt: datetime, end_dt: datetime) -> float:
    if start_dt > end_dt:
        raise ValueError("Start time must be before end time")
    
    total_seconds = (end_dt - start_dt).total_seconds()
    
    hours_decimal = Decimal(str(total_seconds)) / Decimal(str(SECONDS_PER_HOUR))
    
    rounded_hours = float(hours_decimal.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP))
    
    return rounded_hours

if __name__ == '__main__':
    sample_start = datetime(2023, 6, 15, 8, 30, 0)
    sample_end = datetime(2023, 6, 15, 12, 45, 30)
    
    duration = calculate_duration_hours(sample_start, sample_end)
    print(duration)