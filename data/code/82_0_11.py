def calculate_year_difference(year1, year2):
    if not isinstance(year1, int) or not isinstance(year2, int):
        raise ValueError("Inputs must be integers.")
    return abs(year1 - year2)

if __name__ == '__main__':
    year1 = 2023
    year2 = 1998
    try:
        difference = calculate_year_difference(year1, year2)
        print(difference)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)