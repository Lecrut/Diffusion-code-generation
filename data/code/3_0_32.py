import csv

def calculate_average_temperature(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            total_temp = 0
            count = 0
            for row in reader:
                if row and row[0].isdigit():
                    total_temp += float(row[0])
                    count += 1
            if count == 0:
                return 0
            return total_temp / count
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    sample_file_path = 'sample_temperatures.csv'
    average_temperature = calculate_average_temperature(sample_file_path)
    print(average_temperature)