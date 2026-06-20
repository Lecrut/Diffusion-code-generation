ABSOLUTE_DIFFERENCE = 1

def calculate_year_difference(year1, year2):
    return abs(year1 - year2) * ABSOLUTE_DIFFERENCE

if __name__ == '__main__':
    start_year = 2023
    end_year = 1985
    difference = calculate_year_difference(start_year, end_year)
    print(difference)