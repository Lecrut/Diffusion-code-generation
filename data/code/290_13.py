import os
mass_file = "mass_measurements.txt"
output_file = "converted_masses.txt"
sample_masses = [10.5, 25.0, 150.75, 3.14159]
with open(mass_file, 'w') as f:
    for mass in sample_masses:
        f.write(str(mass) + '\n')
with open(mass_file, 'r') as infile:
    for line in infile:
        try:
            mass_kg = float(line.strip())
            mass_g = mass_kg * 1000
            mass_lb = mass_kg * 2.2046226
            output_line = f"{mass_kg}, {mass_g}, {mass_lb}\n"
            with open(output_file, 'a') as outfile:
                outfile.write(output_line)
        except ValueError:
            continue
if __name__ == '__main__':
    pass