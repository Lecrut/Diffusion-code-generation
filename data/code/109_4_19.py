import datetime
import calendar

def get_remaining_hours_in_month(reference_date: datetime.datetime) -> float:
    if reference_date.tzinfo is not None:
        raise ValueError("Timezone-aware dates are not supported.")
    if reference_date.microsecond != 0:
        raise ValueError("Microseconds are not supported for this calculation.")
    
    year = reference_date.year
    month = reference_date.month
    
    last_day_of_month = calendar.monthrange(year, month)[1]
    next_month_first_day = datetime.datetime(year, month + 1, 1) if month < 12 else datetime.datetime(year + 1, 1, 1)
    last_second_of_month = next_month_first_day - datetime.timedelta(seconds=1)
    
    remaining_seconds = (last_second_of_month - reference_date).total_seconds()
    
    if remaining_seconds < 0:
        return 0.0
    
    return remaining_seconds / 3600.0

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 15, 14, 30, 0)
    hours_left = get_remaining_hours_in_month(sample_date)
    print(hours_left)