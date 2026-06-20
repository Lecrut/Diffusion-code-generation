def calculate_year_difference(year1, year2):
    return abs(year1 - year2)

if __name__ == '__main__':
    start_year = 1985
    end_year = 2023
    result = calculate_year_difference(start_year, end_year)
    print(result)