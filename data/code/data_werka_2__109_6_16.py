from datetime import datetime

def fraction_of_month_remaining(start_date: datetime, end_date: datetime) -> float:
    total_seconds = (end_date - start_date).total_seconds()
    current_seconds = (datetime.now() - start_date).total_seconds()
    
    if total_seconds <= 0:
        return 0.0
    
    remaining_seconds = max(0.0, total_seconds - current_seconds)
    fraction = remaining_seconds / total_seconds
    
    return fraction

if __name__ == '__main__':
    start = datetime(2023, 1, 1)
    end = datetime(2023, 12, 31, 23, 59, 59)
    result = fraction_of_month_remaining(start, end)
    print(result)