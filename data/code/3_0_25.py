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
            raise ValueError('No temperature data found in the file.')
        average_temperature = sum(temperatures) / len(temperatures)
        return average_temperature
    except FileNotFoundError:
        print(f'Error: The file {file_path} was not found.')
    except ValueError as ve:
        print(f'ValueError: {ve}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
if __name__ == '__main__':
    sample_file_path = 'sample_temperatures.csv'
    average_temp = calculate_average_temperature(sample_file_path)
    if average_temp is not None:
        print(f'The average temperature is: {average_temp}')