import os
file_path = "mass_measurements.txt"
output_path = "converted_measurements.txt"
sample_data = [10.5, 25.75, 42.0, 150.3]
with open(file_path, 'w') as f:
    for mass in sample_data:
        f.write(str(mass) + '\n')
with open(file_path, 'r') as infile:
    lines = infile.readlines()
with open(output_path, 'w') as outfile:
    for line in lines:
        try:
            mass_kg = float(line.strip())
            mass_g = mass_kg * 1000
            mass_lb = mass_kg * 2.2046226
            outfile.write(f"Original KG: {mass_kg:.3f}, Grams: {mass_g:.3f}, Pounds: {mass_lb:.3f}\n")
        except ValueError:
            continue
if __name__ == '__main__':
    pass