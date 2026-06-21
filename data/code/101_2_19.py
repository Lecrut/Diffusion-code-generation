def get_day_name(year, month, day):
    if not (isinstance(year, int) and isinstance(month, int) and isinstance(day, int)):
        raise ValueError("Arguments must be integers")
    if not (1 <= month <= 12):
        raise ValueError("Month out of range")
    if not (1 <= day <= 31):
        raise ValueError("Day out of range")
    
    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if is_leap:
        month_days[2] = 29
    
    if day > month_days[month]:
        raise ValueError("Invalid day for month")
    
    if month < 3:
        month += 12
        year -= 1
        
    k = year % 100
    j = year // 100
    h = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
    
    names = {
        0: "Saturday",
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday"
    }
    
    return names[h]

if __name__ == '__main__':
    print(get_day_name(2024, 2, 29))