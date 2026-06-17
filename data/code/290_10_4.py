import sys
def convert_mass(value, unit):
    if unit == 'kg':
        if unit == 'kg':
            return value
        elif unit == 'g':
            return value * 1000
        elif unit == 'lb':
            return value * 2.20462
    elif unit == 'g':
        if unit == 'g':
            return value / 1000
        elif unit == 'kg':
            return value / 1000
        elif unit == 'lb':
            return value * 0.00220462
    elif unit == 'lb':
        if unit == 'lb':
            return value
        elif unit == 'kg':
            return value / 2.20462
        elif unit == 'g':
            return value / 0.00220462
    else:
        raise ValueError("Invalid unit specified. Must be 'kg', 'g', or 'lb'.")
if __name__ == '__main__':
    mass_value = 500
    mass_unit = 'g'
    try:
        result = convert_mass(mass_value, mass_unit)
        print(f"Input Mass: {mass_value} {mass_unit}")
        print(f"Converted Mass: {result}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)