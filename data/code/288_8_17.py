def convert_temperatures(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            kelvin = float(line.strip())
            celsius = kelvin - 273.15
            outfile.write(f"{celsius:.2f}\n")

if __name__ == '__main__':
    convert_temperatures('temperatures_kelvin.txt', 'temperatures_celsius.txt')