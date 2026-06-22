def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_days_in_year(year):
    return 366 if is_leap_year(year) else 365

if __name__ == '__main__':
    print(calculate_days_in_year(2023))
    print(calculate_days_in_year(2024))
    print(calculate_days_in_year(2025))