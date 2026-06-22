def days_in_month(year: int, month: int) -> int:
    if not 1 <= year <= 9999 or not 1 <= month <= 12:
        raise ValueError('Year must be between 1 and 9999, and month must be between 1 and 12')
    
    days_per_month = {
        1: 31, 2: 28, 3: 31,
        4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30,
        10: 31, 11: 30, 12: 31
    }
    
    if month == 2:
        is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        return days_per_month[month] + int(is_leap)
    else:
        return days_per_month[month]

if __name__ == '__main__':
    print(days_in_month(2023, 2))
    print(days_in_month(2024, 2))
    print(days_in_month(2023, 4))