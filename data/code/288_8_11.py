KELVIN_TO_CELSIUS = 273.15

def convert_kelvin_to_celsius(temp):
    return temp - KELVIN_TO_CELSIUS

def write_temperatures(input_file, output_file):
    with open(input_file, 'r') as infile:
        temperatures = [float(line.strip()) for line in infile]
    
    converted_temperatures = [convert_kelvin_to_celsius(temp) for temp in temperatures]
    
    with open(output_file, 'w') as outfile:
        for temp in converted_temperatures:
            outfile.write(f"{temp:.2f}°C\n")

if __name__ == '__main__':
    sample_input = "temperatures.txt"
    sample_output = "converted_temperatures.txt"
    write_temperatures(sample_input, sample_output)