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
                print(f"Skipping invalid temperature value: {line.strip()}")
        
        return "\n".join(converted_data)
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {input_file_path} was not found.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while processing the file: {e}")

if __name__ == '__main__':
    sample_input = "sample_temperatures.txt"
    with open(sample_input, 'w') as f:
        f.write("0\n25\n-40\n100\nabc\n37")

    result = convert_temperatures(sample_input)
    print(result)