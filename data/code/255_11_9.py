def find_max_value(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [float(line.strip()) for line in file if line.strip().replace('.', '', 1).isdigit()]
        return max(numbers)
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except ValueError:
        print("Error: Non-numeric data in the file.")
        return None

if __name__ == '__main__':
    sample_values = "data.txt"
    result = find_max_value(sample_values)
    if result is not None:
        print(result)