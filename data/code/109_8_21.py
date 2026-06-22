import datetime
import calendar

def count_weekdays_left_in_month(reference_date: datetime.date) -> int:
    year = reference_date.year
    month = reference_date.month
    day = reference_date.day
    
    _, days_in_month = calendar.monthrange(year, month)
    
    remaining_days = days_in_month - day
    if remaining_days <= 0:
        return 0
    
    current_date = reference_date + datetime.timedelta(days=remaining_days)
    total_weekdays = 0
    
    for i in range(remaining_days + 1):
        check_date = reference_date + datetime.timedelta(days=i)
        if check_date.weekday() < 5:
            total_weekdays += 1
            
    return total_weekdays

if __name__ == '__main__':
    ref_date = datetime.date(2023, 10, 15)
    result = count_weekdays_left_in_month(ref_date)
    print(result)