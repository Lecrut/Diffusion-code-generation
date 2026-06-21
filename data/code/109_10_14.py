import datetime

_DAYS_IN_MONTH = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(year, month):
    if month not in _DAYS_IN_MONTH:
        raise ValueError("Invalid month")
    if month == 2 and is_leap_year(year):
        return 29
    return _DAYS_IN_MONTH[month]

def calculate_days_remaining(year, month, day):
    if month < 1 or month > 12:
        raise ValueError("Month out of range")
    if day < 1 or day > get_days_in_month(year, month):
        raise ValueError("Day out of range")
    
    days_in_month = get_days_in_month(year, month)
    return days_in_month - day

if __name__ == '__main__':
    sample_cases = [
        (2023, 10, 15),
        (2024, 2, 28),
        (2024, 2, 29),
        (2023, 12, 31)
    ]
    
    for y, m, d in sample_cases:
        result = calculate_days_remaining(y, m, d)
        print(result)