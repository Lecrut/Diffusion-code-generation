import argparse

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def batch_convert_temperature(input_file_path):
    try:
        with open(input_file_path, 'r') as file:
            lines = file.readlines()
        
        converted_temperatures = []
        for line in lines:
            try:
                celsius = float(line.strip())
                fahrenheit = celsius_to_fahrenheit(celsius)
                converted_temperatures.append(fahrenheit)
            except ValueError:
                print(f"Error: Invalid temperature value '{line.strip()}' in file.")
        
        return converted_temperatures
    except FileNotFoundError:
        print("Error: File not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

if __name__ == '__main__':
    sample_input_file_path = "sample_temperatures.txt"
    converted_temps = batch_convert_temperature(sample_input_file_path)
    print(converted_temps)