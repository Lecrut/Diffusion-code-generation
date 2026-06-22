def is_leap_year(year: int) -> bool:
    divisibility_by_4 = year % 4 == 0
    divisibility_by_100 = year % 100 == 0
    divisibility_by_400 = year % 400 == 0
    is_century = divisibility_by_400 or (divisibility_by_100 and not divisibility_by_400)
    is_regular_leap = divisibility_by_4 and not divisibility_by_100
    return is_century or is_regular_leap

if __name__ == '__main__':
    sample_years = [2400, 1800, 2024, 1999]
    for year in sample_years:
        print(is_leap_year(year))