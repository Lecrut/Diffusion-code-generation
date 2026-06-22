import argparse

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_temperatures(input_file_path):
    try:
        with open(input_file_path, 'r') as file:
            lines = file.readlines()
        
        converted_data = []
        for line in lines:
            try:
                celsius = float(line.strip())
                fahrenheit = celsius_to_fahrenheit(celsius)
                converted_data.append(f"{celsius}C -> {fahrenheit}F")
            except ValueError:
                raise ValueError(f"Invalid temperature value: {line.strip()}")
        
        return converted_data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at path {input_file_path} was not found.")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

if __name__ == '__main__':
    sample_input = "sample_temperatures.txt"
    try:
        result = convert_temperatures(sample_input)
        for line in result:
            print(line)
    except Exception as e:
        print(e)