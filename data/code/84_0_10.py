def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, is_leap=False):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 29 if is_leap else 28

def calculate_day_of_year(year, month, day):
    if not (1 <= year <= 9999) or not (1 <= month <= 12) or not (1 <= day <= days_in_month(month, is_leap_year(year))):
        return "Invalid date"
    
    days = sum(days_in_month(m, is_leap_year(year)) for m in range(1, month))
    return days + day

if __name__ == '__main__':
    year = 2024
    month = 2
    day = 29
    result = calculate_day_of_year(year, month, day)
    print(result)