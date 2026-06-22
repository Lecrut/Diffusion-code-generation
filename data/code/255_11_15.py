MAX_VALUE_ERROR = "Input file cannot be empty"

def read_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [float(line.strip()) for line in file if line.strip().replace('.', '', 1).isdigit()]
            return numbers
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except ValueError:
        print("Error: Non-numeric data found in the file.")
        return []

def find_maximum(data):
    if not data:
        raise ValueError(MAX_VALUE_ERROR)
    max_val = data[0]
    for x in data[1:]:
        if x > max_val:
            max_val = x
    return max_val

if __name__ == '__main__':
    file_path = 'numbers.txt'
    numbers = read_numbers_from_file(file_path)
    if numbers:
        print(find_maximum(numbers))