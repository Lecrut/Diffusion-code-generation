def validate_years(year1, year2):
    if not isinstance(year1, int) or not isinstance(year2, int):
        raise ValueError("Both inputs must be integers.")
    if year1 < 0 or year2 < 0:
        raise ValueError("Years cannot be negative.")

def find_year_gap(year1, year2):
    validate_years(year1, year2)
    return abs(year1 - year2)

if __name__ == '__main__':
    year_a = 2023
    year_b = 1998
    gap = find_year_gap(year_a, year_b)
    print(gap)