import datetime

def calculate_remaining_hours(target_date: datetime.datetime) -> float:
    if target_date.tzinfo is not None:
        raise ValueError("Timezone-aware datetime objects are not supported.")
    
    end_of_month = datetime.datetime(
        target_date.year,
        target_date.month + 1,
        1
    ) - datetime.timedelta(seconds=1)
    
    delta = end_of_month - target_date
    total_seconds = delta.total_seconds()
    
    if total_seconds < 0:
        return 0.0
    
    return total_seconds / 3600.0

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 15, 14, 30, 0)
    remaining = calculate_remaining_hours(sample_date)
    print(remaining)