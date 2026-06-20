def count_leap_years(start_year, end_year):
    def is_leap(year):
        return (year & 3 == 0) and ((year % 25 != 0) or (year & 15 == 0))

    return sum(is_leap(year) for year in range(start_year, end_year + 1))

if __name__ == '__main__':
    print(count_leap_years(2000, 2023))