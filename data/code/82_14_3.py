def absolute_year_difference(year1: int, year2: int) -> int:
    return abs(year1 - year2)

if __name__ == '__main__':
    sample_year1 = 2045
    sample_year2 = 1967
    print(absolute_year_difference(sample_year1, sample_year2))