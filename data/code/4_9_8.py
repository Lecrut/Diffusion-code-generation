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
            return distance / 0.621371
    else:
        return "Invalid unit specified."
if __name__ == '__main__':
    sample_distance = 10
    sample_unit = 'km'
    converted_value = convert_distance(sample_distance, sample_unit)
    if isinstance(converted_value, float):
        print(f"Original distance: {sample_distance} {sample_unit}")
        print(f"Converted distance: {converted_value:.4f}")
    else:
        print(converted_value)