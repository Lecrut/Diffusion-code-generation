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
            if temperatures:
                return sum(temperatures) / len(temperatures)
            else:
                raise ValueError('No valid temperature data found in the file.')
    except FileNotFoundError:
        raise FileNotFoundError(f'The file {file_path} was not found.')
    except Exception as e:
        raise Exception(f'An error occurred: {e}')
if __name__ == '__main__':
    sample_file_path = 'sample_temperatures.csv'
    try:
        average_temperature = calculate_average_temperature(sample_file_path)
        print(average_temperature)
    except Exception as e:
        print(e)