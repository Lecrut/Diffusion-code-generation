def find_max_value(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [float(line.strip()) for line in file if line.strip().replace('.', '', 1).isdigit()]
            if not numbers:
                return None
            return max(numbers)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except ValueError as e:
        print(f"Error: Invalid data in file. {e}")
        return None

if __name__ == '__main__':
    sample_file_path = 'sample_numbers.txt'
    max_value = find_max_value(sample_file_path)
    if max_value is not None:
        print(f"The maximum value is: {max_value}")