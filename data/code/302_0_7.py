def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False

def days_in_february(year):
    return 29 if is_leap_year(year) else 28

if __name__ == '__main__':
    sample_year = 2024
    print(days_in_february(sample_year))