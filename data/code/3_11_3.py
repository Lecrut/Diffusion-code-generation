import argparse
import os
import csv

CONST_CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0
CONST_FAHRENHEIT_OFFSET = 32.0

class TemperatureConverter:
    def convert_single(self, celsius_value):
        return (celsius_value * CONST_CELSIUS_TO_FAHRENHEIT_FACTOR) + CONST_FAHRENHEIT_OFFSET

    def process_file(self, input_path):
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"File not found: {input_path}")

        results = []
        with open(input_path, mode='r', newline='') as infile:
            reader = csv.DictReader(infile)
            if reader.fieldnames is None:
                raise ValueError("Empty CSV file provided.")
            target_col = 'celsius'
            if target_col not in reader.fieldnames:
                raise ValueError(f"Column '{target_col}' not found in CSV headers.")

            for row_idx, row in enumerate(reader, start=1):
                raw_value = row[target_col]
                if raw_value is None or raw_value.strip() == '':
                    continue
                try:
                    c_val = float(raw_value)
                    f_val = self.convert_single(c_val)
                    results.append({'celsius': c_val, 'fahrenheit': f_val, 'line': row_idx})
                except ValueError:
                    raise ValueError(f"Invalid float data at row {row_idx}: {raw_value}")
        return results

def main():
    converter = TemperatureConverter()
    sample_input_content = """celsius
0
100
37.5
-40
"""
    sample_file_path = "temp_data.csv"
    with open(sample_file_path, "w", newline="") as f:
        f.write(sample_input_content)

    computed_results = converter.process_file(sample_file_path)
    os.remove(sample_file_path)

    print(computed_results[0])
    print(computed_results[1])
    print(computed_results[2])
    print(computed_results[3])

if __name__ == '__main__':
    main()