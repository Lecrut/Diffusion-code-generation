def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def calculate_day_of_year(year, month, day):
    total_days = sum(days_in_month(year, m) for m in range(1, month))
    return total_days + day

if __name__ == '__main__':
    sample_year = 2024
    sample_month = 3
    sample_day = 15
    result = calculate_day_of_year(sample_year, sample_month, sample_day)
    print(result)