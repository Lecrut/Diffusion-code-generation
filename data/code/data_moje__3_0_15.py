import csv
import os

def calculate_average_temperature(file_path):
    if not os.path.exists(file_path):
        return None

    total_temp = 0.0
    count = 0

    try:
        with open(file_path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    temp_str = row.get('temperature')
                    if temp_str is None:
                        continue
                    temp_val = float(temp_str)
                    total_temp += temp_val
                    count += 1
                except ValueError:
                    continue
    except IOError:
        return None

    if count == 0:
        return None

    return total_temp / count

if __name__ == '__main__':
    temp_data = [
        {'temperature': '20.5'},
        {'temperature': '22.1'},
        {'temperature': '19.8'}
    ]

    sample_file = 'sample_temps.csv'

    with open(sample_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['temperature'])
        writer.writeheader()
        for row in temp_data:
            writer.writerow(row)

    result = calculate_average_temperature(sample_file)

    if result is not None:
        print(f"{result:.2f}")
    else:
        print("Error or no data")

    if os.path.exists(sample_file):
        os.remove(sample_file)