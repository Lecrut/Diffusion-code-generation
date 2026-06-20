def calculate_year_difference(year1, year2):
    difference = abs(year1 - year2)
    return difference

if __name__ == '__main__':
    sample_year1 = 2025
    sample_year2 = 1987
    result = calculate_year_difference(sample_year1, sample_year2)
    print(result)