def days_in_month(year, month):
    if month == 2:
        is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        return 29 if is_leap else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def days_remaining(year, month):
    days_per_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_per_month[month - 1] if month == 2 else (days_per_month[month - 1] + (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)))

if __name__ == '__main__':
    print(days_remaining(2023, 2))
    print(days_remaining(2024, 2))
    print(days_remaining(2023, 4))