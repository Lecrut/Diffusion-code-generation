import argparse
def convert_mass(mass, input_unit, output_unit):
    conversion_factors = {
        ('kg', 'g'): 1000,
        ('g', 'kg'): 0.001,
        ('lb', 'kg'): 0.453592,
        ('kg', 'lb'): 2.20462,
    }
    if input_unit == output_unit:
        return mass
    key = (input_unit, output_unit)
    if key in conversion_factors:
        if input_unit == 'kg' and output_unit == 'g':
            return mass * 1000
        elif input_unit == 'g' and output_unit == 'kg':
            return mass * 0.001
        elif input_unit == 'lb' and output_unit == 'kg':
            return mass * 0.453592
        elif input_unit == 'kg' and output_unit == 'lb':
            return mass * 2.20462
    if input_unit == output_unit:
        return mass
    raise ValueError("Unsupported unit conversion.")
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert mass between units.")
    parser.add_argument('mass', type=float, help='The input mass value.')
    parser.add_argument('input_unit', type=str, help='The input unit (e.g., kg, g, lb).')
    parser.add_argument('output_unit', type=str, help='The desired output unit (e.g., kg, g, lb).')
    args = parser.parse_args(['100', 'kg', 'lb'])
    try:
        result = convert_mass(args.mass, args.input_unit, args.output_unit)
        print(f"{args.mass} {args.input_unit} is equal to {result:.4f} {args.output_unit}")
    except ValueError as e:
        print(f"Error: {e}")