def validate_year(year):
    if not isinstance(year, int) or year < 1:
        raise ValueError("Year must be a positive integer.")

def calculate_year_difference(year1, year2):
    validate_year(year1)
    validate_year(year2)
    return abs(year1 - year2)

if __name__ == '__main__':
    try:
        difference = calculate_year_difference(2023, 1998)
        print(difference)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)