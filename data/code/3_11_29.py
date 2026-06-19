import argparse

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_temperatures(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file:
            lines = input_file.readlines()
        
        converted_lines = []
        for line in lines:
            try:
                celsius_value = float(line.strip())
                fahrenheit_value = celsius_to_fahrenheit(celsius_value)
                converted_lines.append(f"{fahrenheit_value}\n")
            except ValueError:
                print(f"Warning: Skipping invalid line '{line.strip()}'")

        with open(output_file_path, 'w') as output_file:
            output_file.writelines(converted_lines)

    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    input_data = """0
25
-40
100
abc
37"""
    sample_input_file_path = "sample_input.txt"
    sample_output_file_path = "sample_output.txt"

    with open(sample_input_file_path, 'w') as f:
        f.write(input_data)

    convert_temperatures(sample_input_file_path, sample_output_file_path)

    with open(sample_output_file_path, 'r') as f:
        print(f.read())