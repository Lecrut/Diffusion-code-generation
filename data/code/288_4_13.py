class TemperatureConverter:
    F_TO_C_FACTOR = 5 / 9
    C_TO_F_OFFSET = 32

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * TemperatureConverter.F_TO_C_FACTOR) + TemperatureConverter.C_TO_F_OFFSET

    @staticmethod
    def process_temperatures(input_file, output_file):
        try:
            with open(input_file, 'r') as infile:
                temperatures = [float(line.strip()) for line in infile]
        except FileNotFoundError:
            print("Input file not found.")
            return

        fahrenheit_temps = [TemperatureConverter.celsius_to_fahrenheit(temp) for temp in temperatures]

        try:
            with open(output_file, 'w') as outfile:
                for temp in fahrenheit_temps:
                    outfile.write(f"{temp}\n")
        except IOError:
            print("Error writing to output file.")

if __name__ == '__main__':
    TemperatureConverter.process_temperatures('temperatures_celsius.txt', 'temperatures_fahrenheit.txt')