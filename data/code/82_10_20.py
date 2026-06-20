START_YEAR = 1985
END_YEAR = 2023

def calculate_year_difference(year1, year2):
    return abs(year1 - year2)
if __name__ == '__main__':
    result = calculate_year_difference(START_YEAR, END_YEAR)
    print(result)