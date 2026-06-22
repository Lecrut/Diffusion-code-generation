import argparse

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_temperatures(input_file_path):
    try:
        with open(input_file_path, 'r') as file:
            lines = file.readlines()
        
        converted_lines = []
        for line in lines:
            try:
                celsius = float(line.strip())
                fahrenheit = celsius_to_fahrenheit(celsius)
                converted_lines.append(f"{fahrenheit}\n")
            except ValueError:
                raise ValueError(f"Invalid temperature value: {line.strip()}")
        
        return ''.join(converted_lines)
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {input_file_path} was not found.")
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}")

if __name__ == '__main__':
    sample_input = "sample_temperatures.txt"
    with open(sample_input, 'w') as f:
        f.write("0\n25\n-40\n100")

    try:
        result = convert_temperatures(sample_input)
        print(result)
    except Exception as e:
        print(e)