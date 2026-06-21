from calendar import day_name

def get_day_of_week(date_string: str) -> int:
    parts = date_string.split("-")
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                days_in_month[2] = 29
            else:
                days_in_month[2] = 28
        else:
            days_in_month[2] = 29
    else:
        days_in_month[2] = 28
        
    if month < 1 or month > 12:
        raise ValueError("Invalid month")
    if day < 1 or day > days_in_month[month]:
        raise ValueError("Invalid day")
        
    if month < 3:
        year -= 1
        m = month + 9
    else:
        m = month - 3
        
    c = year // 100
    y = year % 100
    
    day_of_week = (1 + (13 * m + 8) // 5 + y + y // 4 + c // 4 - 2 * c) % 7
    
    return day_of_week

if __name__ == '__main__':
    result1 = get_day_of_week("2023-10-23")
    print(result1)
    result2 = get_day_of_week("2000-02-29")
    print(result2)
    result3 = get_day_of_week("1999-12-31")
    print(result3)