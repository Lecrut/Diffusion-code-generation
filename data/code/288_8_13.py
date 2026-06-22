def convert_temp_to_celsius(temp_kelvin):
    try:
        temp_celsius = temp_kelvin - 273.15
        return round(temp_celsius, 2)
    except TypeError:
        raise ValueError("Invalid temperature value")

def write_temperatures(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            try:
                temp_kelvin = float(line.strip())
                temp_celsius = convert_temp_to_celsius(temp_kelvin)
                outfile.write(f"{temp_celsius}°C\n")
            except ValueError as e:
                print(e)

if __name__ == '__main__':
    input_file = 'input_temps.txt'
    output_file = 'output_temps.txt'
    write_temperatures(input_file, output_file)