import datetime
import calendar

def get_remaining_weekdays(reference_date: datetime.date) -> int:
    if not isinstance(reference_date, datetime.date):
        raise ValueError("Input must be a datetime.date object")
    
    year = reference_date.year
    month = reference_date.month
    
    if year < 1 or year > 9999:
        raise ValueError("Year out of valid range")
    if month < 1 or month > 12:
        raise ValueError("Month out of valid range")
    if reference_date.day < 1 or reference_date.day > calendar.monthrange(year, month)[1]:
        raise ValueError("Day out of valid range for the given month")
    
    _, days_in_month = calendar.monthrange(year, month)
    
    if reference_date.day > days_in_month:
        return 0
    
    end_date = datetime.date(year, month, days_in_month)
    
    if reference_date > end_date:
        return 0
    
    total_days = (end_date - reference_date).days + 1
    
    start_weekday = reference_date.weekday()
    
    full_weeks, remaining_days = divmod(total_days, 7)
    
    weekdays_in_full_weeks = full_weeks * 5
    
    extra_weekdays = 0
    for i in range(remaining_days):
        current_weekday = (start_weekday + i) % 7
        if current_weekday < 5:
            extra_weekdays += 1
            
    return weekdays_in_full_weeks + extra_weekdays

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    result = get_remaining_weekdays(sample_date)
    print(result)