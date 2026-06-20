def absolute_year_difference(year1: int, year2: int) -> int:
    return abs(year1 - year2)

if __name__ == '__main__':
    sample_years = {'year1': 2060, 'year2': 2000}
    print(absolute_year_difference(sample_years['year1'], sample_years['year2']))