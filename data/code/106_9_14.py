def calculate_year_difference(year1, year2):
    return abs(year1 - year2)

if __name__ == '__main__':
    sample_year1 = 1985
    sample_year2 = 2023
    difference = calculate_year_difference(sample_year1, sample_year2)
    print(difference)