import os
mass_file = "mass_measurements.txt"
output_file = "converted_masses.txt"
sample_masses = [10.5, 22.8, 45.0, 78.9, 150.3]
with open(mass_file, 'w') as f:
    for mass in sample_masses:
        f.write(str(mass) + '\n')
with open(mass_file, 'r') as infile:
    masses = [float(line.strip()) for line in infile]
with open(output_file, 'w') as outfile:
    for mass in masses:
        grams = mass * 1000
        pounds = mass * 2.2046226
        outfile.write(f"{mass:.2f} kg -> {grams:.2f} g, {pounds:.2f} lbs\n")
if __name__ == '__main__':
    pass