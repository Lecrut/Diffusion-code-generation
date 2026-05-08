def calculate_year_difference(end_year, start_year):
    return abs(end_year - start_year)
if __name__ == '__main__':
    year1 = 2024
    year2 = 1990
    difference = calculate_year_difference(year1, year2)
    print(difference)