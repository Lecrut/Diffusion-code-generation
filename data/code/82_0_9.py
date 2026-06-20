def calculate_year_difference(year1, year2):
    return abs(year1 - year2)

if __name__ == '__main__':
    sample_years = {'start': 2000, 'end': 2023}
    difference = calculate_year_difference(sample_years['start'], sample_years['end'])
    print(difference)