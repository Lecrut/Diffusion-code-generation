import csv
import tempfile
import os

def calculate_average_temperature(file_path):
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader, None)
            if header is None:
                raise ValueError("CSV file is empty or has no header.")

            temperature_index = None
            for i, col in enumerate(header):
                if col.strip().lower() == 'temperature':
                    temperature_index = i
                    break

            if temperature_index is None:
                raise ValueError("CSV file does not contain a 'temperature' column.")

            temperatures = []
            for row in reader:
                if len(row) > temperature_index:
                    try:
                        temp_value = float(row[temperature_index])
                        temperatures.append(temp_value)
                    except ValueError:
                        continue

            if not temperatures:
                raise ValueError("No valid temperature data found in the CSV file.")

            average = sum(temperatures) / len(temperatures)
            return average

    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")

if __name__ == '__main__':
    sample_csv_content = "temperature,weather\n22.5,sunny\n18.3,cloudy\n25.1,partly_cloudy\n20.0,rainy\n"

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as temp_file:
        temp_file.write(sample_csv_content)
        temp_file_path = temp_file.name

    try:
        result = calculate_average_temperature(temp_file_path)
        print(result)
    finally:
        os.unlink(temp_file_path)