import datetime
import calendar

def get_month_status(year: int, month: int) -> dict:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    
    today = datetime.date.today()
    current_year = today.year
    current_month = today.month
    current_day = today.day
    
    if year != current_year:
        raise ValueError("Year must match the current year")
    
    days_in_month = calendar.monthrange(year, month)[1]
    
    if month < current_month:
        return {
            "year": year,
            "month": month,
            "days_in_month": days_in_month,
            "days_elapsed": days_in_month,
            "days_remaining": 0,
            "completion_percentage": 100.0
        }
    
    if month == current_month:
        days_elapsed = current_day
        days_remaining = days_in_month - current_day
        completion_percentage = (days_elapsed / days_in_month) * 100
    else:
        days_elapsed = 0
        days_remaining = days_in_month
        completion_percentage = 0.0
    
    return {
        "year": year,
        "month": month,
        "days_in_month": days_in_month,
        "days_elapsed": days_elapsed,
        "days_remaining": days_remaining,
        "completion_percentage": completion_percentage
    }

if __name__ == '__main__':
    result = get_month_status(2023, 10)
    print(result)