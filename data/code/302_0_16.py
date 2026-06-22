def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_february(year):
    if not is_leap_year(year):
        return 28
    else:
        return 29

if __name__ == '__main__':
    sample_year = 2024
    result = days_in_february(sample_year)
    print(result)