YEAR_1 = 2023
YEAR_2 = 1985

def calculate_year_difference(year1, year2):
    return abs(year1 - year2)

if __name__ == '__main__':
    result = calculate_year_difference(YEAR_1, YEAR_2)
    print(result)