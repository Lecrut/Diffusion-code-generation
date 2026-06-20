def calculate_year_difference(year1, year2):
    return abs(year1 - year2)

if __name__ == '__main__':
    year_a = 2024
    year_b = 1985
    difference = calculate_year_difference(year_a, year_b)
    print(difference)