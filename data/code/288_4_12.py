def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def process_temperatures(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            temperatures = [float(line.strip()) for line in infile]
        fahrenheit_temps = [celsius_to_fahrenheit(temp) for temp in temperatures]
        with open(output_file, 'w') as outfile:
            for temp in fahrenheit_temps:
                outfile.write(f"{temp}\n")
    except FileNotFoundError:
        print("Input file not found.")
    except ValueError:
        print("Invalid temperature format.")

if __name__ == '__main__':
    input_path = 'sample_celsius.txt'
    output_path = 'sample_fahrenheit.txt'
    
    sample_temps = [0, 15, 25, 30, 40]
    with open(input_path, 'w') as infile:
        for temp in sample_temps:
            infile.write(f"{temp}\n")
    
    process_temperatures(input_path, output_path)
    
    with open(output_path, 'r') as outfile:
        print(outfile.read())