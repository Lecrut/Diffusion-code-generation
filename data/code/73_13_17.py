from datetime import datetime
from typing import Dict, Any

UNIT_CONVERSIONS: Dict[str, float] = {
    'seconds': 1.0,
    'minutes': 60.0,
    'hours': 3600.0,
    'days': 86400.0
}

def calculate_hours_delta(start: datetime, end: datetime) -> float:
    if start > end:
        raise ValueError("Start time must be before end time")
    
    delta_seconds = (end - start).total_seconds()
    
    conversion_factor = UNIT_CONVERSIONS['hours']
    
    return delta_seconds / conversion_factor

if __name__ == '__main__':
    start_dt = datetime(2024, 1, 15, 6, 0, 0)
    end_dt = datetime(2024, 1, 15, 18, 30, 0)
    
    result = calculate_hours_delta(start_dt, end_dt)
    print(result)