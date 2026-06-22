def is_weekday(date_str):
    year = int(date_str[0:4])
    month = int(date_str[5:7])
    day = int(date_str[8:10])
    
    if month < 1 or month > 12:
        raise ValueError("Invalid month")
    if day < 1 or day > 31:
        raise ValueError("Invalid day")
        
    if month < 3:
        month += 12
        year -= 1
        
    k = year % 100
    j = year // 100
    
    h = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
    
    return h not in (0, 6)

if __name__ == '__main__':
    print(is_weekday("2023-10-07"))
    print(is_weekday("2023-10-08"))
    print(is_weekday("2023-10-09"))