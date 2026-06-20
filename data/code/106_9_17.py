def calculate_year_difference(year1, year2):
    if not isinstance(year1, int) or not isinstance(year2, int):
        raise ValueError('Both inputs must be integers.')
    if year1 < 0 or year2 < 0:
        raise ValueError('Year values must be non-negative.')
    return abs(year1 - year2)
if __name__ == '__main__':
    print(calculate_year_difference(2023, 2018))
    print(calculate_year_difference(1990, 2010))
    print(calculate_year_difference(2024, 2024))