import os
def calculate_equivalent_weight(file_path):
    component_data = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        component_name = parts[0].strip()
                        value = float(parts[1].strip())
                        component_data[component_name] = value
                    except ValueError:
                        print(f"Error: Invalid numeric value found in line: {line.strip()}")
                else:
                    print(f"Warning: Skipping malformed line: {line.strip()}")
        return component_data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during file reading: {e}")
        return None
def calculate_equivalent_weight_mixture(component_data):
    if not component_data:
        return 0.0
    total_mass = sum(component_data.values())
    if total_mass == 0:
        return 0.0
    equivalent_weights = {}
    for name, mass in component_data.items():
        equivalent_weight = (mass / total_mass) * 100                                                            
        equivalent_weights[name] = equivalent_weight
    return equivalent_weights
if __name__ == '__main__':
    sample_file_name = "component_data.txt"
    try:
        with open(sample_file_name, 'w') as f:
            f.write("ComponentA,10.5\n")
            f.write("ComponentB,20.0\n")
            f.write("ComponentC,5.5\n")
            f.write("InvalidData,not_a_number\n")
            f.write("ComponentD,14.0\n")
        component_data = calculate_equivalent_weight(sample_file_name)
        if component_data is not None:
            result = calculate_equivalent_weight_mixture(component_data)
            print("\n--- Component Data Read ---")
            if result:
                for name, ew in result.items():
                    print(f"{name}: {ew:.2f}%")
            else:
                print("No valid data to process.")
        else:
            print("Calculation aborted due to file reading error.")
    except Exception as e:
        print(f"Program execution failed: {e}")
    finally:
        if os.path.exists(sample_file_name):
            os.remove(sample_file_name)