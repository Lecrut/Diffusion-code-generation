def read_floats_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [float(line.strip()) for line in file if line.strip().replace('.', '', 1).isdigit()]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except ValueError:
        print("Error: Non-numeric data encountered in the file.")
        return []

def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_val = max(data)
    return max_val

if __name__ == '__main__':
    sample_file_path = 'sample_numbers.txt'
    numbers = read_floats_from_file(sample_file_path)
    print(find_maximum(numbers))