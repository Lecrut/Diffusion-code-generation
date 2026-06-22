import datetime
import calendar

def get_remaining_hours_in_month(reference_dt: datetime.datetime) -> float:
    if reference_dt.tzinfo is not None:
        raise ValueError("Timezone-aware dates are not supported.")
    
    if reference_dt.month == 12:
        next_month_year = reference_dt.year + 1
        next_month_day = 1
    else:
        next_month_year = reference_dt.year
        next_month_day = reference_dt.month + 1
    
    start_of_next_month = datetime.datetime(next_month_year, next_month_day, 1)
    delta = start_of_next_month - reference_dt
    remaining_seconds = delta.total_seconds()
    
    if remaining_seconds < 0:
        return 0.0
    
    return remaining_seconds / 3600.0

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 15, 14, 30, 0)
    hours_left = get_remaining_hours_in_month(sample_date)
    print(hours_left)