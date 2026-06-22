import calendar

def is_weekday(date_string: str) -> bool:
    DATE_FORMAT = 'YYYY-MM-DD'
    WEEKDAY_THRESHOLD = 5
    MAX_YEAR = 9999
    MIN_YEAR = 1
    
    if not isinstance(date_string, str):
        raise TypeError('Input must be a string')
    
    parts = date_string.split('-')
    if len(parts) != 3:
        raise ValueError(f'Expected format {DATE_FORMAT}')
    
    try:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
    except ValueError:
        raise ValueError('Date components must be integers')
        
    if not (MIN_YEAR <= year <= MAX_YEAR):
        raise ValueError(f'Year must be between {MIN_YEAR} and {MAX_YEAR}')
    if not (1 <= month <= 12):
        raise ValueError('Month must be between 1 and 12')
    if day < 1:
        raise ValueError('Day must be positive')
        
    max_day = calendar.monthrange(year, month)[1]
    if day > max_day:
        raise ValueError(f'Day out of range for month {month} of year {year}')
        
    weekday_index = calendar.weekday(year, month, day)
    return weekday_index < WEEKDAY_THRESHOLD

if __name__ == '__main__':
    sample_date = '2023-10-07'
    result = is_weekday(sample_date)
    print(result)