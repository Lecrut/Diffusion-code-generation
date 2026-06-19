import argparse

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def batch_convert_temperature(input_file_path):
    try:
        with open(input_file_path, 'r') as file:
            lines = file.readlines()
        
        converted_data = []
        for line in lines:
            try:
                celsius_value = float(line.strip())
                fahrenheit_value = celsius_to_fahrenheit(celsius_value)
                converted_data.append(f"{celsius_value}C -> {fahrenheit_value}F")
            except ValueError as e:
                print(f"Error converting line '{line.strip()}': {e}")
        
        return "\n".join(converted_data)
    except FileNotFoundError:
        return f"Error: The file at {input_file_path} was not found."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

if __name__ == '__main__':
    sample_input = "sample_celsius_temperatures.txt"
    result = batch_convert_temperature(sample_input)
    print(result)