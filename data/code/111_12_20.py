def is_leap_year(year):
    return year & 3 == 0 and (year & 15 != 0 or year & 399 == 0)

def count_leap_years(start, end):
    if start > end:
        return 0
    leap_count = sum((is_leap_year(year) for year in range(start, end + 1)))
    return leap_count
if __name__ == '__main__':
    print(count_leap_years(2000, 2023))