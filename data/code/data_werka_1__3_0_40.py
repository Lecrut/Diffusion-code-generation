import csv

def calculate_average_temperature(file_path):
    total_temp = 0
    count = 0
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row and row[0].strip().isdigit():
                    total_temp += float(row[0])
                    count += 1
    except FileNotFoundError:
        print('File not found')
        return None
    except Exception as e:
        print(f'An error occurred: {e}')
        return None
    if count == 0:
        return None
    return total_temp / count
if __name__ == '__main__':
    sample_csv_data = 'Temperature\n23.5\n25.0\n21.2\n22.8'
    with open('temp_readings.csv', 'w') as temp_file:
        temp_file.write(sample_csv_data)
    average_temp = calculate_average_temperature('temp_readings.csv')
    if average_temp is not None:
        print(f'Average Temperature: {average_temp:.2f}')
    else:
        print('Could not calculate average temperature')