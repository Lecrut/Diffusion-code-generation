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
        print('Invalid data in the file.')
        return None
if __name__ == '__main__':
    sample_file_path = 'sample_temperatures.csv'
    average_temp = calculate_average_temperature(sample_file_path)
    if average_temp is not None:
        print(f'Average Temperature: {average_temp:.2f}°C')
    else:
        print('Failed to calculate average temperature.')