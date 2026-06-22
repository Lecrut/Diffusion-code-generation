def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30

def total_days_in_year(year):
    return sum(days_in_month(month, year) for month in range(1, 13))

if __name__ == '__main__':
    print(total_days_in_year(2023))
    print(total_days_in_year(2024))