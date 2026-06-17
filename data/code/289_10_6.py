import sys
def convert_distance(value, from_unit):
    if from_unit == "miles":
        return value * 1.60934
    elif from_unit == "kilometers":
        return value / 1.60934
    else:
        raise ValueError("Invalid unit specified. Must be 'miles' or 'kilometers'.")
if __name__ == '__main__':
    sample_distance = 100
    sample_unit = "miles"
    try:
        numerical_value = float(sample_distance)
        if sample_unit == "miles":
            result = convert_distance(numerical_value, "miles")
            print(f"{sample_distance} miles is equal to {result:.2f} kilometers.")
        elif sample_unit == "kilometers":
            result = convert_distance(numerical_value, "kilometers")
            print(f"{sample_distance} kilometers is equal to {result:.2f} miles.")
        else:
            print("Error: Sample unit is not supported.")
    except ValueError as e:
        print(f"Error processing input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")