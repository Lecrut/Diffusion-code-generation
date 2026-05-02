import sys
def calculate_perimeter(side_a, side_b, side_c):
    return side_a + side_b + side_c
if __name__ == '__main__':
    side_a = 5
    side_b = 12
    side_c = 13
    try:
        if not all(isinstance(side, (int, float)) for side in [side_a, side_b, side_c]):
            raise ValueError("Input sides must be numeric.")
        perimeter = calculate_perimeter(side_a, side_b, side_c)
        print(f"Side A: {side_a}")
        print(f"Side B: {side_b}")
        print(f"Side C: {side_c}")
        print(f"Perimeter: {perimeter}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)