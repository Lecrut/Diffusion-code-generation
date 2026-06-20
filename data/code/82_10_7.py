def calculate_year_difference(year1, year2):
    return abs(year1 - year2)

if __name__ == '__main__':
    start_year = 1970
    end_year = 2023
    difference = calculate_year_difference(start_year, end_year)
    print(difference)