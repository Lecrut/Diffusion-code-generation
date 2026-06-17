import sys
def convert_length(value, unit):
    if unit == "meters":
        if value > 0:
            return value * 3.28084
        else:
            return 0
    elif unit == "feet":
        if value > 0:
            return value / 3.28084
        else:
            return 0
    else:
        raise ValueError("Invalid unit specified")
if __name__ == '__main__':
    sample_length = 10
    sample_unit = "meters"
    try:
        input_value = float(sample_length)
        input_unit = sample_unit
        converted_value = convert_length(input_value, input_unit)
        print(f"{input_value} {input_unit} is equal to {converted_value:.4f} feet")
    except ValueError as e:
        print(f"Error: Invalid input. {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)