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
def calculate_equivalent_weights_stoichiometry(formula_data):
    equivalent_weights = {}
    for formula, atomic_weight in formula_data.items():
        if formula and atomic_weight is not None:
            equivalent_weights[formula] = atomic_weight
    return equivalent_weights
if __name__ == '__main__':
    sample_filename = 'chemical_data.csv'
    sample_data = [
        ['H2O', '18.015'],
        ['CO2', '44.01'],
        ['NaCl', '58.44']
    ]
    try:
        with open(sample_filename, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(sample_data)
        print("--- Reading data from sample file ---")
        formula_weights = calculate_equivalent_weights(sample_filename)
        if formula_weights is not None:
            print("\nCalculated Equivalent Weights (based on input):")
            for formula, weight in formula_weights.items():
                print(f"Compound: {formula}, Weight: {weight}")
    except Exception as e:
        print(f"Script execution failed: {e}")