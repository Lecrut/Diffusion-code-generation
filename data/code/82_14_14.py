def absolute_year_difference(year1: int, year2: int) -> int:
    return abs(year1 - year2)

if __name__ == '__main__':
    sample_years = {1: 2060, 2: 1980}
    print(absolute_year_difference(sample_years[1], sample_years[2]))