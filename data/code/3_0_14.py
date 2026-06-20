import csv
import os
import tempfile

def calculate_average_temperature(csv_file_path):
    temperatures = []
    try:
        with open(csv_file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    temp_value = float(row.get('temperature', 0))
                    temperatures.append(temp_value)
                except (ValueError, TypeError):
                    continue
    except FileNotFoundError:
        return None
    except IOError:
        return None
    except Exception:
        return None

    if not temperatures:
        return None

    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False)
    try:
        writer = csv.DictWriter(temp_file, fieldnames=['timestamp', 'temperature', 'location'])
        writer.writeheader()
        writer.writerow({'timestamp': '2023-01-01 00:00:00', 'temperature': '22.5', 'location': 'Office'})
        writer.writerow({'timestamp': '2023-01-01 01:00:00', 'temperature': '23.1', 'location': 'Office'})
        writer.writerow({'timestamp': '2023-01-01 02:00:00', 'temperature': '21.9', 'location': 'Office'})
        writer.writerow({'timestamp': '2023-01-01 03:00:00', 'temperature': 'invalid', 'location': 'Office'})
        writer.writerow({'timestamp': '2023-01-01 04:00:00', 'temperature': '24.0', 'location': 'Office'})
        temp_file.flush()
        result = calculate_average_temperature(temp_file.name)
        print(result)
    finally:
        temp_file.close()
        os.unlink(temp_file.name)