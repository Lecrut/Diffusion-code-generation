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
        result = convert_distance(sample_distance, sample_unit)
        print(f"Sample Distance: {sample_distance} {sample_unit}")
        print(f"Converted Value: {result}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)