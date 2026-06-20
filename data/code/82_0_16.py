MIN_YEAR = 1900

def calculate_year_difference(year1, year2):
    if year1 < MIN_YEAR or year2 < MIN_YEAR:
        raise ValueError('Both years must be at least 1900.')
    return abs(year1 - year2)
if __name__ == '__main__':
    year1 = 2023
    year2 = 1998
    try:
        difference = calculate_year_difference(year1, year2)
        print(difference)
    except ValueError as e:
        print(f'Error: {e}', file=sys.stderr)