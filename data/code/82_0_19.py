def calculate_year_difference(year1, year2):
    return abs(year1 - year2)

if __name__ == '__main__':
    sample_years = {1: 2023, 2: 1998}
    difference = calculate_year_difference(sample_years[1], sample_years[2])
    print(difference)