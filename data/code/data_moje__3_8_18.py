import csv
import os
import tempfile

CONVERSION_FACTOR = 9 / 5
CONVERSION_OFFSET = 32
TARGET_COLUMN_NAME = 'temp_celsius'
OUTPUT_COLUMN_NAME = 'temp_fahrenheit'

class TemperatureProcessor:
    def __init__(self, input_filepath, output_filepath):
        self.input_filepath = input_filepath
        self.output_filepath = output_filepath

    def celsius_to_fahrenheit(self, value):
        return float(value) * CONVERSION_FACTOR + CONVERSION_OFFSET

    def process(self):
        if not os.path.exists(self.input_filepath):
            raise FileNotFoundError(f"File not found: {self.input_filepath}")

        try:
            with open(self.input_filepath, 'r', newline='', encoding='utf-8') as infile:
                reader = csv.reader(infile)
                header_row = next(reader, None)
                
                if header_row is None:
                    raise ValueError("Input CSV file is empty.")

                if TARGET_COLUMN_NAME not in header_row:
                    raise ValueError(f"Missing required column '{TARGET_COLUMN_NAME}' in CSV header.")

                temp_col_index = header_row.index(TARGET_COLUMN_NAME)
                output_header = list(header_row)
                output_header[temp_col_index] = OUTPUT_COLUMN_NAME

                rows_to_write = [output_header]

                for row in reader:
                    if not row:
                        continue
                    try:
                        celsius_val = row[temp_col_index]
                        fahrenheit_val = self.celsius_to_fahrenheit(celsius_val)
                        new_row = list(row)
                        new_row[temp_col_index] = str(fahrenheit_val)
                        rows_to_write.append(new_row)
                    except (ValueError, IndexError):
                        new_row = list(row)
                        new_row[temp_col_index] = "INVALID"
                        rows_to_write.append(new_row)

            with open(self.output_filepath, 'w', newline='', encoding='utf-8') as outfile:
                writer = csv.writer(outfile)
                writer.writerows(rows_to_write)

            return output_header, len(rows_to_write) - 1

        except IOError as io_err:
            raise RuntimeError(f"File I/O error: {io_err}")

def create_sample_csv(filepath):
    headers = ['date', 'temp_celsius', 'location']
    data = [
        ['2023-10-01', '20.5', 'London'],
        ['2023-10-02', '-5.0', 'Moscow'],
        ['2023-10-03', '30.0', 'Dubai'],
    ]
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)

if __name__ == '__main__':
    temp_input = 'sample_temps.csv'
    temp_output = 'converted_temps.csv'

    create_sample_csv(temp_input)

    processor = TemperatureProcessor(temp_input, temp_output)
    result_header, row_count = processor.process()

    print(result_header)
    print(row_count)

    with open(temp_output, 'r', encoding='utf-8') as f:
        print(f.read())

    os.remove(temp_input)
    os.remove(temp_output)