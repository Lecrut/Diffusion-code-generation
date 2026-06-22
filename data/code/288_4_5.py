def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_temperatures(input_file, output_file):
    with open(input_file, 'r') as file:
        temperatures_celsius = [float(line.strip()) for line in file]

    temperatures_fahrenheit = [celsius_to_fahrenheit(temp) for temp in temperatures_celsius]

    with open(output_file, 'w') as file:
        for temp in temperatures_fahrenheit:
            file.write(f"{temp}\n")

if __name__ == '__main__':
    convert_temperatures('temperatures_celsius.txt', 'temperatures_fahrenheit.txt')