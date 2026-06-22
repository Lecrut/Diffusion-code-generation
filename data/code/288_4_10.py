def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def process_temperature_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        temperatures = [float(line.strip()) for line in infile]
    
    fahrenheit_temperatures = [convert_celsius_to_fahrenheit(temp) for temp in temperatures]
    
    with open(output_file, 'w') as outfile:
        for temp in fahrenheit_temperatures:
            outfile.write(f"{temp}\n")

if __name__ == '__main__':
    process_temperature_file('input.txt', 'output.txt')