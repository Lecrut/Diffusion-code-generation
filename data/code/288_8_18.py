def convert_kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def process_temperatures(input_file, output_file):
    with open(input_file, 'r') as infile:
        temperatures = [float(line.strip()) for line in infile]

    converted_temperatures = [convert_kelvin_to_celsius(temp) for temp in temperatures]

    with open(output_file, 'w') as outfile:
        for temp in converted_temperatures:
            outfile.write(f"{temp:.2f}°C\n")

if __name__ == '__main__':
    input_path = "temperatures_k.txt"
    output_path = "temperatures_c.txt"
    process_temperatures(input_path, output_path)