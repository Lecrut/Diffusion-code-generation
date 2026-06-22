import datetime
import calendar

def get_month_stats(year: int, month: int) -> dict:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    
    today = datetime.date.today()
    current_year = today.year
    current_month = today.month
    current_day = today.day
    
    days_in_month = calendar.monthrange(year, month)[1]
    
    if year < current_year:
        remaining_days = 0
        percentage = 100.0
    elif year == current_year:
        if month < current_month:
            remaining_days = 0
            percentage = 100.0
        elif month == current_month:
            remaining_days = days_in_month - current_day
            percentage = (current_day / days_in_month) * 100.0
        else:
            remaining_days = days_in_month
            percentage = 0.0
    else:
        remaining_days = days_in_month
        percentage = 0.0
        
    return {
        "year": year,
        "month": month,
        "days_in_month": days_in_month,
        "remaining_days": remaining_days,
        "percentage_complete": round(percentage, 2)
    }

if __name__ == '__main__':
    result = get_month_stats(2023, 10)
    print(result)