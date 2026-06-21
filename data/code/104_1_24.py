def get_later_date(date1: str, date2: str) -> str:
    MONTH_DAYS = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    def is_leap(year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def normalize_date(year: int, month: int, day: int) -> int:
        total_days = year * 366 + month * 31 + day
        current_year = 1
        while current_year < year:
            total_days -= 365
            if is_leap(current_year):
                total_days += 1
            current_year += 1
        
        current_month = 1
        while current_month < month:
            days_in_month = MONTH_DAYS[current_month]
            if current_month == 2 and is_leap(year):
                days_in_month = 29
            total_days -= days_in_month
            current_month += 1
        
        total_days -= 1
        return total_days

    parts1 = date1.split('-')
    parts2 = date2.split('-')
    
    if len(parts1) != 3 or len(parts2) != 3:
        raise ValueError("Invalid date format")

    y1, m1, d1 = int(parts1[0]), int(parts1[1]), int(parts1[2])
    y2, m2, d2 = int(parts2[0]), int(parts2[1]), int(parts2[2])

    total_days1 = normalize_date(y1, m1, d1)
    total_days2 = normalize_date(y2, m2, d2)

    if total_days1 >= total_days2:
        return date1
    return date2

if __name__ == '__main__':
    result = get_later_date("2023-10-15", "2023-10-16")
    print(result)