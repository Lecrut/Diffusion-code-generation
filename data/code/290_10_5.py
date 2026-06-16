import sys
def convert_mass(value, unit):
    if unit == 'kg':
        return value
    elif unit == 'g':
        return value / 1000
    elif unit == 'lb':
        return value * 2.20462
    else:
        raise ValueError("Invalid unit specified. Must be 'kg', 'g', or 'lb'.")
if __name__ == '__main__':
    mass_kg = 5.5
    mass_g = 5500
    mass_lb = 120.462
    print("--- Conversion Examples ---")
    try:
        result_kg = convert_mass(mass_kg, 'kg')
        print(f"{mass_kg} kg is equal to {result_kg:.2f} kg")
        result_g = convert_mass(mass_g, 'g')
        print(f"{mass_g} g is equal to {result_g:.2f} kg")
        result_lb = convert_mass(mass_lb, 'lb')
        print(f"{mass_lb} lb is equal to {result_lb:.2f} kg")
    except ValueError as e:
        print(f"Error during conversion: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)