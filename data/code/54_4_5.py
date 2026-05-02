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
            result = calculate_circle_area(radius)
            if result is not None:
                print(result)
            else:
                print("Error: Radius must be a positive number.")
        except ValueError:
            print("Error: Invalid input. Please provide a valid number.")
    else:
        sample_radii = [5.0, 0.0, -2.5, "abc"]
        for sample in sample_radii:
            try:
                radius = float(sample)
                result = calculate_circle_area(radius)
                if result is not None:
                    print(f"Input: {sample}, Area: {result}")
                else:
                    print(f"Input: {sample}, Error: Radius must be a positive number.")
            except ValueError:
                print(f"Input: {sample}, Error: Invalid input format.")