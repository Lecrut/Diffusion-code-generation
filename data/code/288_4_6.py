def validate_temperatures(temperatures):
    if not all(isinstance(temp, (int, float)) for temp in temperatures):
        raise ValueError("All temperatures must be numbers.")

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def process_temperature_file(input_path, output_path):
    validate_temperatures(temperatures := [float(line.strip()) for line in open(input_path)])
    fahrenheit_temps = [celsius_to_fahrenheit(temp) for temp in temperatures]
    with open(output_path, 'w') as outfile:
        for temp in fahrenheit_temps:
            outfile.write(f"{temp}\n")

if __name__ == '__main__':
    process_temperature_file('temperatures_celsius.txt', 'temperatures_fahrenheit.txt')