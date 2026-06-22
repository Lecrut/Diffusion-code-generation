def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def process_temperatures(input_file, output_file):
    with open(input_file, 'r') as infile:
        temperatures = [float(line.strip()) for line in infile]
    
    fahrenheit_temps = [celsius_to_fahrenheit(temp) for temp in temperatures]
    
    with open(output_file, 'w') as outfile:
        for temp in fahrenheit_temps:
            outfile.write(f"{temp}\n")

if __name__ == '__main__':
    process_temperatures('temperatures_celsius.txt', 'temperatures_fahrenheit.txt')