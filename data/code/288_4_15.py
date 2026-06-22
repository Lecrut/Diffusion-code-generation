def convert_temperature(celsius):
    return (celsius * 9/5) + 32

def process_temperatures(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            celsius_readings = [float(line.strip()) for line in infile]
    except FileNotFoundError:
        print("Input file not found.")
        return
    
    fahrenheit_readings = [convert_temperature(c) for c in celsius_readings]
    
    try:
        with open(output_file, 'w') as outfile:
            for f in fahrenheit_readings:
                outfile.write(f"{f}\n")
    except IOError:
        print("Error writing to output file.")

if __name__ == '__main__':
    input_file = 'temperatures_celsius.txt'
    output_file = 'temperatures_fahrenheit.txt'
    
    sample_temps = [0, 10, 20, 25, 30]
    with open(input_file, 'w') as f:
        for temp in sample_temps:
            f.write(f"{temp}\n")
    
    process_temperatures(input_file, output_file)