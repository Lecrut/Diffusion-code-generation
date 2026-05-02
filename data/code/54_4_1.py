import sys
def calculate_circle_area(radius_str):
    try:
        radius = float(radius_str)
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        area = 3.141592653589793 * (radius ** 2)
        return area
    except ValueError as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)
    except Exception as e:
        sys.stderr.write(f"An unexpected error occurred: {e}\n")
        sys.exit(1)
if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_radius = sys.argv[1]
    else:
        input_radius = "10.0"
    calculate_circle_area(input_radius)