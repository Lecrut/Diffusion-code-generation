def calculate_year_difference(year1, year2):
    if not isinstance(year1, int) or not isinstance(year2, int):
        raise ValueError("Inputs must be integers.")
    return abs(year1 - year2)

if __name__ == '__main__':
    try:
        difference = calculate_year_difference(2023, 1998)
        print(difference)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)