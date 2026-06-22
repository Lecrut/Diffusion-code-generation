import datetime
import calendar

def get_month_progress(year: int, month: int) -> dict:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if year < 1:
        raise ValueError("Year must be positive")

    today = datetime.date.today()
    current_year = today.year
    current_month = today.month
    current_day = today.day

    days_in_month = calendar.monthrange(year, month)[1]
    
    if year < current_year:
        total_days = days_in_month
        remaining_days = 0
        completed_days = days_in_month
    elif year == current_year and month < current_month:
        total_days = days_in_month
        remaining_days = 0
        completed_days = days_in_month
    elif year == current_year and month == current_month:
        completed_days = current_day
        remaining_days = days_in_month - current_day
        total_days = days_in_month
    else:
        total_days = days_in_month
        remaining_days = days_in_month
        completed_days = 0

    if total_days == 0:
        percentage = 0.0
    else:
        percentage = (completed_days / total_days) * 100

    return {
        "year": year,
        "month": month,
        "total_days": total_days,
        "completed_days": completed_days,
        "remaining_days": remaining_days,
        "percentage": round(percentage, 2)
    }

if __name__ == '__main__':
    result = get_month_progress(2023, 10)
    print(result)