import datetime

def calculate_remaining_hours(target_date: datetime.datetime) -> float:
    if target_date.tzinfo is not None:
        raise ValueError("Timezone-aware dates are not supported for this calculation.")
    
    start_of_next_month = target_date.replace(day=1)
    start_of_next_month = start_of_next_month + datetime.timedelta(days=32)
    start_of_next_month = start_of_next_month.replace(day=1)
    
    remaining_seconds = (start_of_next_month - target_date).total_seconds()
    return remaining_seconds / 3600

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 15, 10, 30, 0)
    hours_remaining = calculate_remaining_hours(sample_date)
    print(hours_remaining)