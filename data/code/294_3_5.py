import os
def calculate_equivalent_weight(component_data):
    total_equivalent_weight = 0.0
    for component in component_data:
        try:
            mass = float(component['mass'])
            moles = float(component['moles'])
            if mass < 0 or moles < 0:
                raise ValueError("Mass and moles must be non-negative.")
            if moles == 0:
                equivalent_weight = float('inf') if mass > 0 else 0.0
            else:
                equivalent_weight = mass / moles
            total_equivalent_weight += equivalent_weight
        except (ValueError, TypeError) as e:
            print(f"Error processing component data: {component}. Error: {e}")
            return None
    return total_equivalent_weight
def read_component_data(filepath):
    component_list = []
    if not os.path.exists(filepath):
        print(f"Error: File not found at {filepath}")
        return None
    try:
        with open(filepath, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    component_list.append({
                        'mass': parts[0],
                        'moles': parts[1]
                    })
                elif line.strip():
                    print(f"Warning: Skipping malformed line in file: {line.strip()}")
        return component_list
    except IOError as e:
        print(f"Error reading file {filepath}: {e}")
        return None
if __name__ == '__main__':
    FILE_NAME = "component_data.txt"
    sample_data = [
        {"mass": "100.0", "moles": "2.0"},
        {"mass": "50.0", "moles": "1.0"},
        {"mass": "200.0", "moles": "4.0"},
        {"mass": "-10.0", "moles": "1.0"}                          
    ]
    try:
        with open(FILE_NAME, 'w') as f:
            for item in sample_data:
                f.write(f"{item['mass']},{item['moles']}\n")
        print("--- Reading data from file ---")
        component_data = read_component_data(FILE_NAME)
        if component_data is not None:
            print("\n--- Calculating Equivalent Weight ---")
            final_weight = calculate_equivalent_weight(component_data)
            if final_weight is not None:
                print(f"\nFinal Equivalent Weight of the mixture: {final_weight}")
            else:
                print("\nCalculation failed due to input errors.")
    except Exception as e:
        print(f"An unexpected error occurred during execution: {e}")