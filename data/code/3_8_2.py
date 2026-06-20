import csv
import os

def convert_celsius_to_fahrenheit(input_filepath: str, output_filepath: str) -> list[float]:
    readings = []
    try:
        with open(input_filepath, mode='r', newline='') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                celsius_value = float(row['celsius'])
                fahrenheit_value = celsius_value * 9 / 5 + 32
                readings.append(fahrenheit_value)
    except FileNotFoundError:
        return []
    except KeyError as e:
        return []
    except ValueError:
        return []
    try:
        with open(output_filepath, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['fahrenheit'])
            for f_val in readings:
                writer.writerow([f_val])
    except IOError:
        return []
    return readings
if __name__ == '__main__':
    input_file = 'input_temps.csv'
    output_file = 'output_temps.csv'
    with open(input_file, 'w', newline='') as tmpf:
        writer = csv.writer(tmpf)
        writer.writerow(['celsius'])
        writer.writerow([0.0])
        writer.writerow([100.0])
        writer.writerow([36.6])
    fahrenheit_values = convert_celsius_to_fahrenheit(input_file, output_file)
    print(fahrenheit_values)
    if os.path.exists(input_file):
        os.remove(input_file)
    if os.path.exists(output_file):
        os.remove(output_file)