import datetime
import calendar

def compute_remaining_hours(date_instance: datetime.datetime) -> float:
    if date_instance.tzinfo is not None:
        raise ValueError("Timezone-aware dates are not supported.")
    year = date_instance.year
    month = date_instance.month
    last_day = calendar.monthrange(year, month)[1]
    next_month_start = datetime.datetime(year, month + 1, 1) if month < 12 else datetime.datetime(year + 1, 1, 1)
    end_of_current_month = next_month_start - datetime.timedelta(days=1)
    end_of_current_month = end_of_current_month.replace(hour=23, minute=59, second=59, microsecond=999999)
    time_delta = end_of_current_month - date_instance
    total_seconds = time_delta.total_seconds()
    if total_seconds < 0:
        return 0.0
    return total_seconds / 3600

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 15, 14, 30, 0)
    hours_left = compute_remaining_hours(sample_date)
    print(hours_left)