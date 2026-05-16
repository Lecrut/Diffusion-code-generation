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
    raise ValueError("Invalid unit specified. Must be 'm', 'km', or 'mi'.")
if __name__ == '__main__':
    sample_value = 5000.0
    from_unit = 'm'
    to_unit = 'km'
    try:
        result = convert_distance(sample_value, from_unit, to_unit)
        print(f"{sample_value} {from_unit} is equal to {result:.4f} {to_unit}")
        sample_value_2 = 10.0
        from_unit_2 = 'mi'
        to_unit_2 = 'm'
        result_2 = convert_distance(sample_value_2, from_unit_2, to_unit_2)
        print(f"{sample_value_2} {from_unit_2} is equal to {result_2:.4f} {to_unit_2}")
        sample_value_3 = 100.0
        from_unit_3 = 'km'
        to_unit_3 = 'mi'
        result_3 = convert_distance(sample_value_3, from_unit_3, to_unit_3)
        print(f"{sample_value_3} {from_unit_3} is equal to {result_3:.4f} {to_unit_3}")
        sample_value_4 = 100.0
        from_unit_4 = 'm'
        to_unit_4 = 'mi'
        result_4 = convert_distance(sample_value_4, from_unit_4, to_unit_4)
        print(f"{sample_value_4} {from_unit_4} is equal to {result_4:.4f} {to_unit_4}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)