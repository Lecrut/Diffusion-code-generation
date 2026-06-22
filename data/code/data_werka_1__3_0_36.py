import csv

def calculate_average_temperature(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            temperatures = []
            for row in reader:
                if row:
                    temperature = float(row[0])
                    temperatures.append(temperature)
        if not temperatures:
            return None
        average_temperature = sum(temperatures) / len(temperatures)
        return average_temperature
    except FileNotFoundError:
        print('File not found.')
        return None
    except ValueError:
        print('Invalid data in the file.')
        return None
    except Exception as e:
        print(f'An error occurred: {e}')
        return None
if __name__ == '__main__':
    sample_csv_content = '23.5\n24.0\n22.8\n23.9'
    with open('sample_temperatures.csv', 'w') as temp_file:
        temp_file.write(sample_csv_content)
    average_temp = calculate_average_temperature('sample_temperatures.csv')
    print(f'Average Temperature: {average_temp}')