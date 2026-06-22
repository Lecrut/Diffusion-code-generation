from datetime import datetime, timedelta

UNIT_LABELS = {
    'days': 86400,
    'hours': 3600,
    'minutes': 60,
    'seconds': 1
}

class TimeCalculator:
    def compute_delta(self, start: datetime, end: datetime) -> dict:
        if not isinstance(start, datetime) or not isinstance(end, datetime):
            raise ValueError("Inputs must be datetime objects")
        
        delta = end - start
        total_seconds = int(delta.total_seconds())
        
        if total_seconds < 0:
            total_seconds = abs(total_seconds)
            sign = -1
        else:
            sign = 1
            
        result = {}
        current_seconds = total_seconds
        
        for unit, seconds_per_unit in UNIT_LABELS.items():
            count = current_seconds // seconds_per_unit
            result[unit] = count * sign
            current_seconds %= seconds_per_unit
            
        return result

if __name__ == '__main__':
    calculator = TimeCalculator()
    t1 = datetime(2023, 1, 1, 10, 0, 0)
    t2 = datetime(2023, 1, 5, 14, 30, 45)
    delta_result = calculator.compute_delta(t1, t2)
    print(delta_result)