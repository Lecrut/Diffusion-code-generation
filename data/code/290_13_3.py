def convert_mass(kg):
    grams = kg * 1000
    pounds = kg * 2.204622
    return grams, pounds
if __name__ == '__main__':
    input_filename = "mass_measurements.txt"
    output_filename = "converted_measurements.txt"
    sample_data = [1.5, 10.25, 500.75, 0.001]
    with open(input_filename, 'w') as f:
        for mass in sample_data:
            f.write(str(mass) + "\n")
    with open(input_filename, 'r') as infile:
        kg_values = []
        for line in infile:
            try:
                kg_values.append(float(line.strip()))
            except ValueError:
                continue
    with open(output_filename, 'w') as outfile:
        for kg in kg_values:
            grams, pounds = convert_mass(kg)
            outfile.write(f"{kg},{grams},{pounds}\n")