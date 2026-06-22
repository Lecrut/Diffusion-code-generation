class TemperatureConverter:
    C_TO_F_FACTOR = 9 / 5
    C_TO_F_OFFSET = 32

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * TemperatureConverter.C_TO_F_FACTOR) + TemperatureConverter.C_TO_F_OFFSET

    @classmethod
    def process_temperatures(cls, input_file, output_file):
        try:
            with open(input_file, 'r') as infile:
                temperatures = [float(line.strip()) for line in infile]
            fahrenheit_temps = [cls.celsius_to_fahrenheit(temp) for temp in temperatures]
            with open(output_file, 'w') as outfile:
                for temp in fahrenheit_temps:
                    outfile.write(f"{temp}\n")
        except FileNotFoundError:
            print("Input file not found.")
        except ValueError:
            print("Invalid temperature format.")

if __name__ == '__main__':
    TemperatureConverter.process_temperatures('temperatures_celsius.txt', 'temperatures_fahrenheit.txt')