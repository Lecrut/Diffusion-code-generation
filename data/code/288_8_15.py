class TemperatureConverter:
    KELVIN_TO_CELSIUS = -273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin + TemperatureConverter.KELVIN_TO_CELSIUS

def convert_temperatures(input_file, output_file):
    with open(input_file, 'r') as infile:
        temperatures = [float(line.strip()) for line in infile]

    converted_temps = [TemperatureConverter.kelvin_to_celsius(temp) for temp in temperatures]

    with open(output_file, 'w') as outfile:
        for temp in converted_temps:
            outfile.write(f"{temp:.2f}°C\n")

if __name__ == '__main__':
    input_path = 'input.txt'
    output_path = 'output.txt'
    convert_temperatures(input_path, output_path)