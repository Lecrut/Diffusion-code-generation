def convert_temperatures(input_file, output_file):
    with open(input_file, 'r') as infile:
        temperatures = [float(line.strip()) for line in infile]

    converted_temperatures = [(temp - 273.15) for temp in temperatures]

    with open(output_file, 'w') as outfile:
        for temp in converted_temperatures:
            outfile.write(f"{temp:.2f}°C\n")

if __name__ == '__main__':
    convert_temperatures('input.txt', 'output.txt')