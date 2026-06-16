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
        print(f"Error converting data to float: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during file reading: {e}")
        return None
    return data
def calculate_stoichiometric_equivalent_weights(formula_data):
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
        ['NaCl', '58.44'],
        ['H2S', '34.08']
    ]
    try:
        with open(sample_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(sample_data)
        print("--- Reading data from sample CSV ---")
        formula_weights = calculate_equivalent_weights(sample_filename)
        if formula_weights:
            print("\nCalculated Equivalent Weights (Placeholder based on input):")
            for formula, weight in formula_weights.items():
                print(f"Compound: {formula}, Weight: {weight}")
            final_results = calculate_stoichiometric_equivalent_weights(formula_weights)
            print("\nFinal Stoichiometric Equivalent Weights:")
            for compound, eq_weight in final_results.items():
                print(f"{compound}: {eq_weight}")
    except Exception as e:
        print(f"Script execution failed: {e}")