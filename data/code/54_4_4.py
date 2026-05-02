import sys
def calculate_circle_area(radius):
    if radius > 0:
        return 3.141592653589793 * radius * radius
    else:
        raise ValueError("Radius must be a positive number.")
if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            radius = float(sys.argv[1])
            area = calculate_circle_area(radius)
            print(f"{area}")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        sample_radii = [5.0, 0.0, -2.5, "abc"]
        for r in sample_radii:
            try:
                radius = float(r)
                area = calculate_circle_area(radius)
                print(f"Input: {r}, Area: {area}")
            except ValueError as e:
                print(f"Input: {r}, Error: {e}", file=sys.stderr)
            except Exception as e:
                print(f"An unexpected error occurred for input {r}: {e}", file=sys.stderr)