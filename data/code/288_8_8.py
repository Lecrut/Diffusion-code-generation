def convert_kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def process_temperatures(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            try:
                kelvin = float(line.strip())
                celsius = convert_kelvin_to_celsius(kelvin)
                outfile.write(f"{celsius:.2f}\n")
            except ValueError:
                print("Invalid temperature value encountered.")

if __name__ == '__main__':
    process_temperatures('temperatures_k.txt', 'temperatures_c.txt')