import datetime
import calendar

def calculate_remaining_minutes_in_current_month(reference_dt):
    year = reference_dt.year
    month = reference_dt.month
    last_day = calendar.monthrange(year, month)[1]
    end_of_month_dt = datetime.datetime(year, month, last_day, 23, 59, 59)
    if reference_dt > end_of_month_dt:
        return 0
    difference = end_of_month_dt - reference_dt
    total_seconds = int(difference.total_seconds())
    if total_seconds > 0:
        total_minutes = total_seconds // 60
        if total_seconds % 60 > 0:
            total_minutes += 1
        return total_minutes
    return 0

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 15, 10, 30, 45)
    result = calculate_remaining_minutes_in_current_month(sample_date)
    print(result)