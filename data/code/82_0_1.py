import sys
def calculate_difference(year1, year2):
    return abs(year1 - year2)
if __name__ == '__main__':
    year1 = 2023
    year2 = 1998
    try:
        if not isinstance(year1, int) or not isinstance(year2, int):
            raise ValueError("Inputs must be integers.")
        difference = calculate_difference(year1, year2)
        print(difference)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)