def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == '__main__':
    years = [2000, 1900, 2024, 2023, 400]
    for y in years:
        print(is_leap_year(y))