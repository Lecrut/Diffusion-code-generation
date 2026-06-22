MAX_FLOAT = float('inf')

def read_floats_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [float(line.strip()) for line in file if line.strip().replace('.', '', 1).isdigit()]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except ValueError:
        print("Error: Non-numeric data found in the file.")
        return []

def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_val = MIN_FLOAT
    for x in data:
        if x > max_val:
            max_val = x
    return max_val

if __name__ == '__main__':
    sample_file_path = 'sample_numbers.txt'
    numbers = read_floats_from_file(sample_file_path)
    if numbers:
        try:
            max_value = find_maximum(numbers)
            print(f"The maximum value is: {max_value}")
        except ValueError as e:
            print(e)