def absolute_year_difference(year1: int, year2: int) -> int:
    if not isinstance(year1, int) or not isinstance(year2, int):
        raise ValueError("Both inputs must be integers")
    return abs(year1 - year2)

if __name__ == '__main__':
    sample_year1 = 2060
    sample_year2 = 1950
    print(absolute_year_difference(sample_year1, sample_year2))