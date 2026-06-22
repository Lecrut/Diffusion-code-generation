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
            except ValueError:
                print(f"Invalid temperature value: {line.strip()}")
        
        return converted_data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {input_file_path} was not found.")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

if __name__ == '__main__':
    sample_input = "sample_temperatures.txt"
    with open(sample_input, 'w') as f:
        f.write("0\n25\n-40\n100\nabc")

    try:
        result = batch_convert_temperature(sample_input)
        for line in result:
            print(line)
    except Exception as e:
        print(e)