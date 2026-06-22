def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_febuary(year):
    if is_leap_year(year):
        return 29
    else:
        return 28

if __name__ == '__main__':
    year = 2023
    print(days_in_febuary(year))