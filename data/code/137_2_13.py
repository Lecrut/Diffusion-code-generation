def is_leap_year(year):
    divisible_by_4 = year % 4 == 0
    not_divisible_by_100 = year % 100 != 0
    divisible_by_400 = year % 400 == 0
    return (divisible_by_4 and not_divisible_by_100) or divisible_by_400

if __name__ == '__main__':
    sample_years = [2000, 1900, 2020, 2021]
    results = {year: is_leap_year(year) for year in sample_years}
    print(results)