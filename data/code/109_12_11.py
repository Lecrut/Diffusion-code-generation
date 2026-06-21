import datetime
import calendar

def get_month_stats(year: int, month: int) -> dict:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    
    now = datetime.datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day
    
    if year != current_year or month != current_month:
        raise ValueError("Year and month must match the current date")
    
    days_in_month = calendar.monthrange(year, month)[1]
    total_days = days_in_month
    days_passed = current_day
    remaining_days = total_days - days_passed
    
    percentage_completed = (days_passed / total_days) * 100
    
    return {
        "year": year,
        "month": month,
        "total_days": total_days,
        "days_passed": days_passed,
        "remaining_days": remaining_days,
        "percentage_completed": percentage_completed
    }

if __name__ == '__main__':
    result = get_month_stats(datetime.datetime.now().year, datetime.datetime.now().month)
    print(result)