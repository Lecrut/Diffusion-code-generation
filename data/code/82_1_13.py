def calculate_year_difference(year1, year2):
    difference = abs(year1 - year2)
    return difference

if __name__ == '__main__':
    start_year = 2024
    end_year = 1999
    result = calculate_year_difference(start_year, end_year)
    print(result)