import csv

def calculate_average_temperature(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            total_temp = 0
            count = 0
            for row in reader:
                if len(row) > 0 and row[0].replace('.', '', 1).isdigit():
                    total_temp += float(row[0])
                    count += 1
            if count == 0:
                return None
            return total_temp / count
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    sample_file_path = 'sample_temperatures.csv'
    average_temperature = calculate_average_temperature(sample_file_path)
    if average_temperature is not None:
        print(f"The average temperature is: {average_temperature:.2f}°C")
    else:
        print("Could not calculate the average temperature.")