def calculate_year_difference(year1, year2):
    return abs(year2 - year1)
if __name__ == '__main__':
    print(calculate_year_difference(2000, 2020))
    print(calculate_year_difference(1990, 2010))
    print(calculate_year_difference(2020, 2000))
    print(calculate_year_difference(2010, 2000))
    print(calculate_year_difference(2000, 2000))
    print(calculate_year_difference(100, 2000))
    print(calculate_year_difference(1000, 500))