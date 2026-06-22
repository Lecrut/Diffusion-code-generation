def days_remaining(year):
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    days_in_february = 29 if is_leap_year else 28
    return days_in_february

if __name__ == '__main__':
    sample_year = 2023
    print(days_remaining(sample_year))