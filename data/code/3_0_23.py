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
        print('Error: The file was not found.')
        return None
    except ValueError:
        print('Error: Invalid data in the file.')
        return None
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return None
if __name__ == '__main__':
    sample_file_path = 'sample_temperatures.csv'
    average_temp = calculate_average_temperature(sample_file_path)
    if average_temp is not None:
        print(f'The average temperature is: {average_temp:.2f}°C')