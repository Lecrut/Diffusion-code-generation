def find_max_value(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [float(line.strip()) for line in file if line.strip().replace('.', '', 1).isdigit()]
            return max(numbers)
    except FileNotFoundError:
        print("File not found.")
        return None
    except ValueError:
        print("Non-numeric data encountered.")
        return None

if __name__ == '__main__':
    sample_file_path = 'sample_numbers.txt'
    result = find_max_value(sample_file_path)
    if result is not None:
        print(result)