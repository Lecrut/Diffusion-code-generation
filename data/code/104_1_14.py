def get_later_date(date1: str, date2: str) -> str:
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    def is_leap_year(year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def parse_to_tuple(date_str: str) -> tuple:
        parts = date_str.split('-')
        if len(parts) != 3:
            raise ValueError("Invalid date format")
        return int(parts[0]), int(parts[1]), int(parts[2])

    def count_days_from_epoch(year: int, month: int, day: int) -> int:
        total_days = 0
        for y in range(1, year):
            if is_leap_year(y):
                total_days += 366
            else:
                total_days += 365
        
        for m in range(1, month):
            if m == 2 and is_leap_year(year):
                total_days += 29
            else:
                total_days += days_in_month[m]
        
        total_days += day
        return total_days

    d1_tuple = parse_to_tuple(date1)
    d2_tuple = parse_to_tuple(date2)
    
    d1_days = count_days_from_epoch(d1_tuple[0], d1_tuple[1], d1_tuple[2])
    d2_days = count_days_from_epoch(d2_tuple[0], d2_tuple[1], d2_tuple[2])
    
    if d1_days > d2_days:
        return date1
    elif d2_days > d1_days:
        return date2
    else:
        return date1

if __name__ == '__main__':
    result = get_later_date("2023-10-15", "2023-10-16")
    print(result)