import datetime
import calendar

def count_weekdays_left_in_month(reference_date: datetime.date) -> int:
    year = reference_date.year
    month = reference_date.month
    day = reference_date.day
    
    _, days_in_month = calendar.monthrange(year, month)
    
    total_days_left = days_in_month - day
    if total_days_left <= 0:
        return 0
    
    current_date = reference_date + datetime.timedelta(days=total_days_left)
    end_date = datetime.date(year, month, days_in_month)
    
    weekdays_count = 0
    current = reference_date
    while current <= end_date:
        if current.weekday() < 5:
            weekdays_count += 1
        current += datetime.timedelta(days=1)
        
    return weekdays_count

if __name__ == '__main__':
    ref_date = datetime.date(2023, 10, 15)
    result = count_weekdays_left_in_month(ref_date)
    print(result)