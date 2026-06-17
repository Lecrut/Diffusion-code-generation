import argparse
def convert_mass(mass, input_unit, output_unit):
    conversion_factors = {
        ('kg', 'g'): 1000,
        ('lb', 'kg'): 2.20462,
        ('g', 'kg'): 0.001,
        ('kg', 'lb'): 0.453592,
        ('lb', 'g'): 453.592,
    }
    if input_unit == output_unit:
        return mass
    key = (input_unit, output_unit)
    if key in conversion_factors:
        if input_unit == 'kg' and output_unit == 'g':
            result = mass * 1000
        elif input_unit == 'g' and output_unit == 'kg':
            result = mass * 0.001
        elif input_unit == 'lb' and output_unit == 'kg':
            result = mass * 2.20462
        elif input_unit == 'kg' and output_unit == 'lb':
            result = mass * 2.20462
        elif input_unit == 'lb' and output_unit == 'g':
            result = mass * 453.592
        else:
            return "Error: Conversion not directly supported for this pair."
        return result
    else:
        return "Error: Conversion between specified units is not supported by this program."
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert mass between different units.")
    parser.add_argument("mass", type=float, help="The input mass value.")
    parser.add_argument("input_unit", type=str, help="The unit of the input mass (e.g., kg, lb, g).")
    parser.add_argument("output_unit", type=str, help="The desired output unit (e.g., kg, lb, g).")
    args = parser.parse_args(["10", "kg", "lb"])
    result = convert_mass(args.mass, args.input_unit, args.output_unit)
    print(f"{args.mass} {args.input_unit} is equal to {result:.4f} {args.output_unit}")