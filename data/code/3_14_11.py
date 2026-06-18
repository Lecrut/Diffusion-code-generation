#!/usr/bin/env python3
"""
CLI script to batch convert temperature data from Celsius to Fahrenheit.
Uses argparse for argument parsing but avoids required arguments via default values,
ensuring it runs without user input or pre-existing files when using the sample block.
"""

import json

def celsius_to_fahrenheit(celcius: float) -> float:
    """Convert a temperature value from Celsius to Fahrenheit."""
    return (celcius * 9 / 5) + 32

def process_batch(input_file_path: str, output_format: str = "json") -> None:
    """Read temperatures from the input file and write converted values to stdout or file.

    Args:
        input_file_path (str): Path to the input CSV/JSON file containing Celsius data.
        output_format (str): Output format ('json' for JSON-LINES, default 'json').
    
    Raises:
        FileNotFoundError: If the specified input file does not exist.
        ValueError: If the temperature value is invalid or non-numeric.
        PermissionError: If there are issues reading/writing files due to permissions.
    """

    if output_format.lower() == "json":
        with open(input_file_path, 'r', encoding='utf-8') as file_in:
            raw_data = [line.strip() for line in file_in.readlines()]

        try:
            data_lines = []
            success_count = 0
            
            for idx, line in enumerate(raw_data):
                if not line or "temperature" not in str(line).lower(): 
                    # Skip lines that are just keys without values (like the header)
                    continue
                    
                temp_str = float("inf")
                
                try:
                    temperature = float(line.split()[1])  # Assume CSV format with a second column
                    fahrenheit_temp = celsius_to_fahrenheit(temperature)

                    data_lines.append(json.dumps({"input": round(temp, 2), "output": round(fahrenheit_temp, 2)}))
                    success_count += 1
                    
                except ValueError:
                    print(f"Error in line {idx + 1}: Invalid temperature value found", file=__import__('sys').stderr)

            if data_lines and output_format.lower() == 'json': 
                # Output JSON-Lines format to stdout for batch efficiency without intermediate files
                print('\n'.join(data_lines), end='')
                
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: Input file '{input_file_path}' not found.") from None
        except PermissionError as e:
            raise PermissionError("Error: Insufficient permissions to read input or write output.", str(e))

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    # Simulates reading a small dataset locally
    
    import sys
    
    class MockFile:
        """Mock file object simulating the CSV input structure."""
        
        def read(self):
            return [
                "temperature,celcius\n",
                "-15.02,-43.986\n", # 4 digits precision for negative values to ensure output is accurate and correct 
                "-27.77,-82.082"   # -27.77 + 32 = 4.23, *1.8/5? No wait: (c*9)/5+32
            ]

        def write(self):
            pass

    # Mock object for file reading and writing to stdout
    input_path_str = "/dev/null" # Preventing network access or local disk dependencies in tests