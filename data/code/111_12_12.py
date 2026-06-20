def count_leap_years(start_year, end_year):
    leap_count = 0
    for year in range(start_year, end_year + 1):
        if (year & 3) == 0 and ((year % 25 != 0) or (year & 15) == 0):
            leap_count += 1
    return leap_count

if __name__ == '__main__':
    print(count_leap_years(2000, 2020))