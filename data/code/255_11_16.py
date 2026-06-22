def read_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [float(line.strip()) for line in file]
            if not numbers:
                raise ValueError("File is empty")
            return numbers
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []
    except ValueError as e:
        print(f"Error: Invalid data in the file - {e}")
        return []

def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_val = data[0]
    for x in data[1:]:
        if x > max_val:
            max_val = x
    return max_val

if __name__ == '__main__':
    file_path = 'numbers.txt'
    numbers = read_numbers_from_file(file_path)
    if numbers:
        print(f"Maximum value: {find_maximum(numbers)}")