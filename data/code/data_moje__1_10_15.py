import csv
import io
import os

def calculate_average_weight_from_csv(file_path):
    weights = []
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if not row:
                    continue
                for value in row:
                    stripped_value = value.strip()
                    if not stripped_value:
                        continue
                    try:
                        weights.append(float(stripped_value))
                    except ValueError:
                        continue
    except FileNotFoundError:
        return None
    except IOError:
        return None
    
    if not weights:
        return None
    
    return sum(weights) / len(weights)

def create_sample_csv(content, filename):
    with open(filename, 'w', newline='') as f:
        f.write(content)

if __name__ == '__main__':
    sample_csv_content = "10.5\n20.3\ninvalid\n30.2\n5.0\nbad_data\n"
    sample_filename = "sample_weights.csv"
    
    create_sample_csv(sample_csv_content, sample_filename)
    
    average = calculate_average_weight_from_csv(sample_filename)
    
    if average is not None:
        print(average)
    else:
        print("No valid weights found.")
    
    os.remove(sample_filename)