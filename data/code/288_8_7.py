def convert_kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Temperature below absolute zero is not possible.")
    return kelvin - 273.15

def process_temperatures(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            temperatures = [float(line.strip()) for line in infile]

        with open(output_file, 'w') as outfile:
            for temp in temperatures:
                celsius_temp = convert_kelvin_to_celsius(temp)
                outfile.write(f"{celsius_temp:.2f}°C\n")

    except FileNotFoundError:
        print("Input file not found.")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    input_file = 'temperatures.txt'
    output_file = 'converted_temperatures.txt'
    process_temperatures(input_file, output_file)