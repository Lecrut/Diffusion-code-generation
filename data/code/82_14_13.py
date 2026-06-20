def validate_years(year1: int, year2: int) -> None:
    if not isinstance(year1, int) or not isinstance(year2, int):
        raise ValueError("Both inputs must be integers")
    if year1 < 0 or year2 < 0:
        raise ValueError("Years must be non-negative")

def absolute_year_difference(year1: int, year2: int) -> int:
    validate_years(year1, year2)
    return abs(year1 - year2)

if __name__ == '__main__':
    sample_year1 = 2060
    sample_year2 = 1980
    print(absolute_year_difference(sample_year1, sample_year2))