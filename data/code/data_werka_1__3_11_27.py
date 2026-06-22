import argparse

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_temperatures(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
            for line in input_file:
                try:
                    celsius = float(line.strip())
                    fahrenheit = celsius_to_fahrenheit(celsius)
                    output_file.write(f"{fahrenheit}\n")
                except ValueError:
                    print(f"Error: Non-numeric value found and skipped - {line.strip()}")
    except FileNotFoundError:
        print("Error: Input file not found.")
    except IOError as e:
        print(f"IO Error: {e}")

if __name__ == '__main__':
    input_data = """0
25
100
-40
abc"""
    output_file_path = "output.txt"
    
    with open("input.txt", "w") as f:
        f.write(input_data)
    
    convert_temperatures("input.txt", output_file_path)