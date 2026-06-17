import sys
def convert_distance(miles, conversion_factor):
    kilometers = miles * conversion_factor
    return kilometers
if __name__ == '__main__':
    sample_miles = 100
    conversion_rate = 1.60934
    try:
        mile_value = float(sample_miles)
        if mile_value < 0:
            raise ValueError("Distance cannot be negative.")
        result_km = convert_distance(mile_value, conversion_rate)
        print(f"Miles to convert: {mile_value}")
        print(f"Conversion factor (miles to km): {conversion_rate}")
        print(f"Result in kilometers: {result_km}")
    except ValueError as e:
        print(f"Error: Invalid input provided. Details: {e}", file=sys.stderr)
    except TypeError:
        print("Error: Input must be a valid number.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)