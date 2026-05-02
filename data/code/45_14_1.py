import sys
if __name__ == '__main__':
    try:
        radius_str = "5.0"
        radius = float(radius_str)
        area = 3.141592653589793 * (radius ** 2)
        print(area)
    except ValueError:
        print("Error: Invalid input provided.", file=sys.stderr)