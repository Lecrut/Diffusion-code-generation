import sys
def calculate_circle_area(radius):
    if radius > 0:
        return 3.141592653589793 * (radius ** 2)
    else:
        return None
if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            radius = float(sys.argv[1])
            area = calculate_circle_area(radius)
            if area is not None:
                print(area)
            else:
                print("Error: Radius must be a positive number.")
        except ValueError:
            print("Error: Invalid input. Please provide a valid number.")
    else:
        sample_radii = [5.0, 0.0, -2.5, "abc"]
        for r in sample_radii:
            try:
                radius = float(r)
                area = calculate_circle_area(radius)
                if area is not None:
                    print(f"Input Radius: {radius}, Area: {area}")
            except ValueError:
                print(f"Input '{r}' caused a ValueError during processing.")