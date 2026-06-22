from datetime import datetime

def is_date_earlier(first_date: datetime, second_date: datetime) -> bool:
    first_year = first_date.year
    first_month = first_date.month
    first_day = first_date.day
    second_year = second_date.year
    second_month = second_date.month
    second_day = second_date.day
    
    if first_year < second_year:
        return True
    if first_year > second_year:
        return False
    
    if first_month < second_month:
        return True
    if first_month > second_month:
        return False
    
    if first_day < second_day:
        return True
    if first_day > second_day:
        return False
    
    first_hour = first_date.hour
    first_minute = first_date.minute
    first_second = first_date.second
    second_hour = second_date.hour
    second_minute = second_date.minute
    second_second = second_date.second
    
    if first_hour < second_hour:
        return True
    if first_hour > second_hour:
        return False
    
    if first_minute < second_minute:
        return True
    if first_minute > second_minute:
        return False
    
    if first_second < second_second:
        return True
    
    return False

if __name__ == '__main__':
    sample_start = datetime(2023, 10, 5, 14, 30, 0)
    sample_end = datetime(2023, 10, 5, 14, 30, 0)
    comparison_result = is_date_earlier(sample_start, sample_end)
    print(comparison_result)