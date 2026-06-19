import csv

def calculate_average_temperature(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            temperatures = []
            for row in reader:
                if row:
                    temperatures.append(float(row[0]))
            if not temperatures:
                return None
            average_temperature = sum(temperatures) / len(temperatures)
            return average_temperature
    except FileNotFoundError:
        print('File not found.')
        return None
    except ValueError:
        print('Invalid data in file.')
        return None
if __name__ == '__main__':
    sample_file_path = 'sample_temperatures.csv'
    sample_data = '23.5\n25.0\n22.8\n24.1\n23.9'
    with open(sample_file_path, 'w') as file:
        file.write(sample_data)
    average_temp = calculate_average_temperature(sample_file_path)
    print(average_temp)