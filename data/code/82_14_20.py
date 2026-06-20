def absolute_year_difference(year1: int, year2: int) -> int:
    return abs(year1 - year2)

if __name__ == '__main__':
    sample_year1 = 2070
    sample_year2 = 1955
    print(absolute_year_difference(sample_year1, sample_year2))