def is_leap_year(year):
    return (year % 400) == 0 and year % 100 != 0 or year % 4 == 0
if __name__ == '__main__':
    sample_years = [2000, 2004, 2008, 2097, 2100]
    for y in sample_years:
        if is_leap_year(y):
            print(f"{y} is a leap year.")
        else:
            print(f"{y} is not a leap year.")