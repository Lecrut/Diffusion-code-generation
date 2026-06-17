import argparse
def convert_mass(mass, input_unit, output_unit):
    conversion_factors = {
        ('kg', 'g'): 1000,
        ('lb', 'kg'): 2.2046226218,
        ('g', 'kg'): 0.001,
        ('lb', 'kg'): 0.45359237,
    }
    if input_unit == output_unit:
        return mass
    key = (input_unit, output_unit)
    if key in conversion_factors:
        if input_unit == 'kg' and output_unit == 'g':
            result = mass * 1000
        elif input_unit == 'g' and output_unit == 'kg':
            result = mass / 1000
        else:
            factor = conversion_factors[key]
            if input_unit == 'lb' and output_unit == 'kg':
                result = mass * factor
            elif input_unit == 'kg' and output_unit == 'lb':
                result = mass / factor
            else:
                result = mass * factor
        return result
    else:
        raise ValueError("Unsupported unit conversion.")
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert mass between different units.")
    parser.add_argument("mass", type=float, help="The input mass value.")
    parser.add_argument("input_unit", type=str, help="The unit of the input mass (e.g., kg, lb, g).")
    parser.add_argument("output_unit", type=str, help="The desired output unit (e.g., kg, lb, g).")
    args = parser.parse_args(["10", "lb", "kg"])
    try:
        result = convert_mass(args.mass, args.input_unit, args.output_unit)
        print(f"{args.mass} {args.input_unit} is equal to {result:.4f} {args.output_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")