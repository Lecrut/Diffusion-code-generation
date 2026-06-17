import csv
def calculate_equivalent_weights(filename):
    data = {}
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    formula = row[0].strip()
                    weight = float(row[1].strip())
                    data[formula] = weight
                else:
                    print(f"Skipping malformed row: {row}")
    except FileNotFoundError:
        print(f"Error: File not found at {filename}")
        return None
    except ValueError as e:
        print(f"Error converting data to number in file: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during file reading: {e}")
        return None
    return data
def calculate_stoichiometric_equivalent_weights(formula_data, atomic_weights):
    equivalent_weights = {}
    for formula, total_weight in formula_data.items():
        if formula in atomic_weights:
            equivalent_weights[formula] = total_weight
        else:
            equivalent_weights[formula] = "Unknown (Atomic Weight Missing)"
    return equivalent_weights
if __name__ == '__main__':
    sample_filename = 'chemical_data.csv'
    sample_data = [
        ['H2O', '18.015'],
        ['CO2', '44.01'],
        ['NaCl', '58.44'],
        ['Fe', '55.845']
    ]
    try:
        with open(sample_filename, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(sample_data)
        formula_weights = calculate_equivalent_weights(sample_filename)
        if formula_weights is not None:
            atomic_weights = {
                'H': 1.008,
                'O': 15.999,
                'C': 12.011,
                'Na': 22.990,
                'Cl': 35.453,
                'Fe': 55.845
            }
            equivalent_weights = calculate_stoichiometric_equivalent_weights(formula_weights, atomic_weights)
            print("--- Calculated Equivalent Weights ---")
            for formula, eq_weight in equivalent_weights.items():
                print(f"{formula}: {eq_weight}")
    except Exception as e:
        print(f"Script execution failed: {e}")