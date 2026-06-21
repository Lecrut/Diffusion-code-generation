import datetime

def calculate_remaining_hours(target_date: datetime.datetime) -> float:
    if target_date.tzinfo is not None:
        raise ValueError("Timezone-aware dates are not supported for this calculation.")
    
    start_of_next_month = target_date.replace(day=1)
    start_of_next_month = start_of_next_month + datetime.timedelta(days=32)
    start_of_next_month = start_of_next_month.replace(day=1)
    
    remaining_seconds = (start_of_next_month - target_date).total_seconds()
    remaining_hours = remaining_seconds / 3600
    
    return remaining_hours

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 15, 14, 30, 0)
    result = calculate_remaining_hours(sample_date)
    print(result)