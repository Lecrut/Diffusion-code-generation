def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_year(year):
    if not isinstance(year, int) or year < 1:
        raise ValueError("Year must be a positive integer")
    return 366 if is_leap_year(year) else 365

if __name__ == '__main__':
    print(days_in_year(2023))
    print(days_in_year(2024))