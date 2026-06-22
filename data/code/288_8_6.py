def convert_kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def process_temperatures(input_file, output_file):
    with open(input_file, 'r') as infile:
        temperatures = [float(line.strip()) for line in infile]
    
    celsius_temperatures = [convert_kelvin_to_celsius(temp) for temp in temperatures]
    
    with open(output_file, 'w') as outfile:
        for temp in celsius_temperatures:
            outfile.write(f"{temp:.2f}\n")

if __name__ == '__main__':
    process_temperatures('temperatures.txt', 'celsius_temperatures.txt')