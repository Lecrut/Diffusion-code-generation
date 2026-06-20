def count_leap_years(start_year, end_year):
    start = max(1582, start_year)
    return (end_year - start) // 4 - (end_year - start) // 100 + (end_year - start) // 400
if __name__ == '__main__':
    print(count_leap_years(1900, 2023))