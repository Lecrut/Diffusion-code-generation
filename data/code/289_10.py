import sys
def convert_distance(distance, unit):
    if unit == 'to_km':
        return distance * 1.60934
    elif unit == 'to_miles':
        return distance / 1.60934
    else:
        raise ValueError("Invalid unit specified. Use 'to_km' or 'to_miles'.")
if __name__ == '__main__':
    sample_distance = 100
    sample_unit = 'to_km'
    try:
        distance_value = float(sample_distance)
        if sample_unit == 'to_km':
            result = convert_distance(distance_value, 'to_km')
            print(f"Original distance: {sample_distance} miles")
            print(f"Converted distance: {result:.2f} kilometers")
        elif sample_unit == 'to_miles':
            result = convert_distance(distance_value, 'to_miles')
            print(f"Original distance: {sample_distance} miles")
            print(f"Converted distance: {result:.2f} miles")
        else:
            print("Error: Sample unit is not recognized.")
    except ValueError as e:
        print(f"Error processing input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")