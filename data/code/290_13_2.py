import os
file_path = "mass_measurements.txt"
output_path = "converted_measurements.txt"
sample_data = [10.5, 25.0, 45.75, 100.0]
with open(file_path, 'w') as f:
    for mass in sample_data:
        f.write(str(mass) + '\n')
with open(file_path, 'r') as infile:
    masses = [float(line.strip()) for line in infile]
with open(output_path, 'w') as outfile:
    for mass in masses:
        grams = mass * 1000
        pounds = mass * 2.2046226
        outfile.write(f"Original Mass (kg): {mass}\n")
        outfile.write(f"Mass (g): {grams:.2f}\n")
        outfile.write(f"Mass (lb): {pounds:.2f}\n")
if __name__ == '__main__':
    pass