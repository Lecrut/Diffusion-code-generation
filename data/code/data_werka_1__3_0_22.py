import csv

def calculate_average_temperature(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            temperatures = []
            for row in reader:
                if row:
                    try:
                        temperature = float(row[0])
                        temperatures.append(temperature)
                    except ValueError:
                        continue
            if not temperatures:
                raise ValueError('No valid temperature data found.')
            return sum(temperatures) / len(temperatures)
    except FileNotFoundError:
        raise FileNotFoundError(f'The file {file_path} does not exist.')
    except IOError as e:
        raise IOError(f'An error occurred while reading the file: {e}')
if __name__ == '__main__':
    sample_file_path = 'sample_temperatures.csv'
    try:
        average_temperature = calculate_average_temperature(sample_file_path)
        print(average_temperature)
    except Exception as e:
        print(e)