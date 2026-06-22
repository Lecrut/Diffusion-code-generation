import calendar

def get_weekday_name_for_date(date_tuple):
    if not isinstance(date_tuple, (list, tuple)) or len(date_tuple) != 3:
        raise ValueError("Expected a sequence of three integers: (year, month, day)")
    
    year, month, day = date_tuple
    
    if not (isinstance(year, int) and isinstance(month, int) and isinstance(day, int)):
        raise TypeError("Year, month, and day must be integers")
        
    try:
        weekday_index = calendar.weekday(year, month, day)
    except ValueError:
        raise ValueError(f"Invalid date: {year}-{month}-{day}")
    
    return calendar.day_name[weekday_index]

if __name__ == '__main__':
    date_sample = (2024, 12, 25)
    print(get_weekday_name_for_date(date_sample))