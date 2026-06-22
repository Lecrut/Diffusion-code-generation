def convert_temperatures(input_file, output_file):
    with open(input_file, 'r') as infile:
        temperatures = [float(line.strip()) for line in infile]

    converted_temps = [(temp - 273.15) for temp in temperatures]

    with open(output_file, 'w') as outfile:
        for temp in converted_temps:
            outfile.write(f"{temp:.2f}°C\n")

if __name__ == '__main__':
    convert_temperatures('temperatures_kelvin.txt', 'temperatures_celsius.txt')