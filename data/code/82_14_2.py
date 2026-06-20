def absolute_year_difference(year1: int, year2: int) -> int:
    difference = year1 - year2
    return abs(difference)

if __name__ == '__main__':
    sample_year1 = 2030
    sample_year2 = 1975
    print(absolute_year_difference(sample_year1, sample_year2))