def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if __name__ == '__main__':
    years_to_check = [2000, 1900, 2024, 2023]
    for y in years_to_check:
        print(is_leap_year(y))