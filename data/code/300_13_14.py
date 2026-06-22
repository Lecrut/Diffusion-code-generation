def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_february(year):
    if is_leap_year(year):
        return 29
    else:
        return 28

if __name__ == '__main__':
    sample_year = 2023
    remaining_days = days_in_february(sample_year)
    print(remaining_days)