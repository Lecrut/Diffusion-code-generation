import sys
def convert_distance(distance, unit):
    if unit == 'km':
        if distance == 0:
            return 0.0
        elif distance == 1:
            return 0.621371
        else:
            return distance * 0.621371
    elif unit == 'mi':
        if distance == 0:
            return 0.0
        elif distance == 1:
            return 1.609344
        else:
            return distance * 1.609344
    else:
        raise ValueError("Invalid unit specified. Use 'km' or 'mi'.")
if __name__ == '__main__':
    sample_distance = 10
    sample_unit = 'km'
    try:
        if sample_unit == 'km':
            result = convert_distance(sample_distance, 'km')
            print(f"Sample Distance: {sample_distance} km")
            print(f"Conversion to miles: {result:.4f} mi")
        elif sample_unit == 'mi':
            result = convert_distance(sample_distance, 'mi')
            print(f"Sample Distance: {sample_distance} mi")
            print(f"Conversion to kilometers: {result * 1.609344:.4f} km")
        else:
            print("Error: Invalid sample unit.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")