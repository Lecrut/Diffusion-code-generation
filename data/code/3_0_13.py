import csv
import os

def calculate_average_temperature(filename):
    temperatures = []
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} not found")
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader, None)
            for row in reader:
                if len(row) >= 1 and row[0].strip():
                    try:
                        temp = float(row[0])
                        temperatures.append(temp)
                    except ValueError:
                        continue
        if not temperatures:
            return None
        return sum(temperatures) / len(temperatures)
    except FileNotFoundError:
        raise
    except PermissionError:
        raise
    except Exception as e:
        raise RuntimeError(f"Error processing file: {e}")

def create_sample_csv(filename, data):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Temperature'])
            for value in data:
                writer.writerow([value])
    except Exception as e:
        raise RuntimeError(f"Error creating sample file: {e}")

if __name__ == '__main__':
    sample_filename = 'sample_temps.csv'
    sample_data = [20.5, 21.3, 19.8, 22.1, 20.0, 21.5]
    create_sample_csv(sample_filename, sample_data)
    result = calculate_average_temperature(sample_filename)
    print(result)
    if os.path.exists(sample_filename):
        os.remove(sample_filename)