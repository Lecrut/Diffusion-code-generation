import datetime

def calculate_remaining_hours(target_date: datetime.datetime) -> float:
    if target_date.tzinfo is not None:
        raise ValueError("Timezone-aware dates are not supported for this calculation.")
    
    end_of_month = datetime.datetime(
        target_date.year,
        target_date.month + 1 if target_date.month < 12 else 1,
        1,
        1,
        0,
        0
    )
    
    if target_date.month == 12:
        end_of_month = datetime.datetime(
            target_date.year + 1,
            1,
            1,
            1,
            0,
            0
        )
    
    remaining_seconds = (end_of_month - target_date).total_seconds()
    
    if remaining_seconds < 0:
        return 0.0
    
    return remaining_seconds / 3600

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 15, 14, 30, 0)
    result = calculate_remaining_hours(sample_date)
    print(result)