def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

if __name__ == '__main__':
    sample_years = [2000, 1900, 2020, 2021]
    for year in sample_years:
        print(f"Year: {year}, Leap Year: {is_leap_year(year)}")