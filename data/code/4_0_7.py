import sys
def convert_distance(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'm':
        if to_unit == 'km':
            return value / 1000.0
        elif to_unit == 'mi':
            return value / 1609.34
    elif from_unit == 'km':
        if to_unit == 'm':
            return value * 1000.0
        elif to_unit == 'mi':
            return value / 1.60934
    elif from_unit == 'mi':
        if to_unit == 'km':
            return value * 1.60934
        elif to_unit == 'm':
            return value * 1609.34
    raise ValueError("Invalid unit specified. Supported units are 'm', 'km', 'mi'.")
if __name__ == '__main__':
    sample_value = 500
    from_unit = 'km'
    to_unit = 'mi'
    try:
        result = convert_distance(sample_value, from_unit, to_unit)
        print(f"{sample_value} {from_unit} is equal to {result:.4f} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)