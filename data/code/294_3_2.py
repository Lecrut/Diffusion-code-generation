import sys
def calculate_equivalent_weight(component_data):
    total_equivalent_weight = 0.0
    for component in component_data:
        try:
            mass = float(component['mass'])
            moles = float(component['moles'])
            if mass < 0 or moles < 0:
                raise ValueError("Mass and moles must be non-negative.")
            equivalent_weight = mass * component['equivalent_weight']
            total_equivalent_weight += equivalent_weight
        except (ValueError, KeyError) as e:
            print(f"Error processing component data: {component}. Error: {e}", file=sys.stderr)
            return None
    return total_equivalent_weight
def read_and_calculate(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.", file=sys.stderr)
        return None
    component_data = []
    for i, line in enumerate(lines):
        try:
            parts = line.strip().split(',')
            if len(parts) != 3:
                raise ValueError("Incorrect number of fields.")
            component_data.append({
                'mass': parts[0],
                'moles': parts[1],
                'equivalent_weight': float(parts[2])
            })
        except ValueError as e:
            print(f"Error parsing line {i+1}: '{line.strip()}'. Error: {e}", file=sys.stderr)
            return None
    if not component_data:
        return 0.0
    result = calculate_equivalent_weight(component_data)
    return result
if __name__ == '__main__':
    sample_filename = "component_data.txt"
    try:
        with open(sample_filename, 'w') as f:
            f.write("10.0,2.0,5.0\n")
            f.write("15.0,3.0,6.0\n")
            f.write("5.0,1.0,4.0\n")
            f.write("invalid_data\n")
            f.write("20.0,4.0,7.0\n")
        final_weight = read_and_calculate(sample_filename)
        if final_weight is not None:
            print(f"The final equivalent weight of the mixture is: {final_weight}")
        else:
            print("Calculation failed due to input errors.")
    except Exception as e:
        print(f"An unexpected error occurred during setup or execution: {e}", file=sys.stderr)