def calculate_year_difference(year1, year2):
    return abs(year1 - year2)

if __name__ == '__main__':
    years = {'year1': 2024, 'year2': 1999}
    difference = calculate_year_difference(years['year1'], years['year2'])
    print(difference)