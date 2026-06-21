def get_day_of_month(year: int, month: int, day: int) -> int:
    if not all(isinstance(v, int) and not isinstance(v, bool) for v in (year, month, day)):
        raise ValueError("Inputs must be integers")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if day < 1:
        raise ValueError("Day must be positive")
    
    month_lengths = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    max_day = month_lengths[month]
    if month == 2 and is_leap:
        max_day += 1
        
    if day > max_day:
        raise ValueError("Day out of range for the given month and year")
        
    return day

if __name__ == '__main__':
    y, m, d = 2024, 2, 29
    day_val = get_day_of_month(y, m, d)
    print(day_val)