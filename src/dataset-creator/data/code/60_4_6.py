def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    else:
        return year % 400 == 0
if __name__ == '__main__':
    sample_years = [2000, 1900, 2024, 2023]
    for y in sample_years:
        result = "Leap" if is_leap_year(y) else "Not Leap"
        print(f"{y}: {result}")