import sys
def calculate_equivalent_weight(component_data):
    total_equivalent_weight = 0.0
    for component in component_data:
        if not isinstance(component, dict) or 'mass' not in component or 'equivalent_weight' not in component:
            print(f"Error: Invalid component data found: {component}", file=sys.stderr)
            continue
        try:
            mass = float(component['mass'])
            eqw = float(component['equivalent_weight'])
            total_equivalent_weight += mass * eqw
        except ValueError:
            print(f"Error: Non-numeric values found in component data: {component}", file=sys.stderr)
            continue
    return total_equivalent_weight
def read_component_data(filename):
    component_list = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        mass = float(parts[0].strip())
                        eqw = float(parts[1].strip())
                        component_list.append({'mass': mass, 'equivalent_weight': eqw})
                    except ValueError:
                        print(f"Error processing line in file: '{line.strip()}' - non-numeric values found.", file=sys.stderr)
                elif line.strip():
                     print(f"Warning: Skipping malformed line in file: '{line.strip()}'", file=sys.stderr)
    except FileNotFoundError:
        print(f"Error: File not found: {filename}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}", file=sys.stderr)
        return None
    return component_list
if __name__ == '__main__':
    filename = "component_data.txt"
    sample_data = [
        {"mass": 10.0, "equivalent_weight": 5.0},
        {"mass": 20.0, "equivalent_weight": 10.0},
        {"mass": 5.0, "equivalent_weight": 2.5},
        {"mass": "invalid", "equivalent_weight": 4.0},                              
        {"mass": 30.0, "equivalent_weight": "error"},                            
        {"mass": 15.0, "equivalent_weight": 7.5}
    ]
    print("--- Processing Hardcoded Sample Data ---")
    component_data = sample_data
    final_ew = calculate_equivalent_weight(component_data)
    if final_ew is not None:
        print("\nCalculation Complete.")
        print(f"Final Equivalent Weight of the mixture: {final_ew}")