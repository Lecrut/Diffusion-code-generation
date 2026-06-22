def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def process_temperatures(input_file, output_file):
    with open(input_file, 'r') as infile:
        temperatures_c = [float(line.strip()) for line in infile]
    
    temperatures_f = [celsius_to_fahrenheit(temp) for temp in temperatures_c]
    
    with open(output_file, 'w') as outfile:
        for temp in temperatures_f:
            outfile.write(f"{temp}\n")

if __name__ == '__main__':
    process_temperatures('temperatures_c.txt', 'temperatures_f.txt')