def get_day_of_month(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Inputs must be integers")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if day < 1:
        raise ValueError("Day must be positive")
    
    days_in_month_map = {
        1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }
    
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    max_day = days_in_month_map[month]
    
    if month == 2 and is_leap:
        max_day = 29
        
    if day > max_day:
        raise ValueError("Day out of range for the given month and year")
        
    return day

if __name__ == '__main__':
    sample_year = 2024
    sample_month = 2
    sample_day = 29
    result = get_day_of_month(sample_year, sample_month, sample_day)
    print(result)