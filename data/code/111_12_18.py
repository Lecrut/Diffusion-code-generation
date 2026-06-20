def is_leap_year(year):
    return (year & 3 == 0) and ((year >> 2) & 15 == 0 or year & 15 == 0)

def count_leap_years(start, end):
    leap_count = 0
    for year in range(start, end + 1):
        if is_leap_year(year):
            leap_count += 1
    return leap_count

if __name__ == '__main__':
    start_year = 2000
    end_year = 2023
    print(count_leap_years(start_year, end_year))