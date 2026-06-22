from datetime import datetime, timedelta

START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2023, 12, 31)

def get_remaining_time_in_month(reference_date: datetime) -> timedelta:
    if reference_date.year != START_DATE.year or reference_date.month != START_DATE.month:
        raise ValueError("Reference date must be within the specified month.")
    
    if reference_date.day == START_DATE.day:
        return timedelta(days=0)
    
    next_month_start = reference_date.replace(day=1) + timedelta(days=32)
    next_month_start = next_month_start.replace(day=1)
    
    days_in_month = (next_month_start - reference_date).days
    days_passed = (reference_date - START_DATE).days
    
    remaining_days = days_in_month - days_passed
    
    return timedelta(days=remaining_days)

if __name__ == '__main__':
    sample_date = datetime(2023, 1, 15)
    result = get_remaining_time_in_month(sample_date)
    print(result)