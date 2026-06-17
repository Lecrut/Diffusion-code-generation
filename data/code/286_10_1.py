import sys
def meters_to_feet(meters):
    if not isinstance(meters, (int, float)):
        raise TypeError("Input must be a numeric value.")
    return meters * 3.28084
if __name__ == '__main__':
    sample_meters = 10
    try:
        feet = meters_to_feet(sample_meters)
        print(f"{sample_meters} meters is equal to {feet:.2f} feet")
    except TypeError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)