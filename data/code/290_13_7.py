import os
mass_file = "mass_measurements.txt"
output_file = "converted_masses.txt"
sample_masses = [10.5, 25.0, 100.0, 5.75]
with open(mass_file, 'w') as f:
    for mass in sample_masses:
        f.write(str(mass) + '\n')
with open(mass_file, 'r') as infile:
    for line in infile:
        try:
            mass_kg = float(line.strip())
            mass_g = mass_kg * 1000
            mass_lb = mass_kg * 2.2046226
            with open(output_file, 'a') as outfile:
                outfile.write(f"{mass_kg:.4f} kg -> {mass_g:.2f} g, {mass_lb:.2f} lb\n")
        except ValueError:
            continue
if __name__ == '__main__':
    pass