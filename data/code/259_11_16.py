def read_data(filename):
    try:
        with open(filename, 'r') as file:
            data = [int(line.strip()) for line in file]
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except ValueError:
        print("Error: Invalid data in file. Please ensure each line contains a valid integer.")
        return []

def write_data(filename, data):
    try:
        with open(filename, 'w') as file:
            for value in data:
                file.write(f"{value}\n")
    except IOError:
        print(f"Error: Failed to write to file '{filename}'.")

def find_min_max(data):
    if not data:
        return None, None
    return min(data), max(data)

if __name__ == '__main__':
    input_filename = 'input.txt'
    output_filename = 'output.txt'

    sample_data = read_data(input_filename)
    minimum, maximum = find_min_max(sample_data)
    
    result_data = [minimum, maximum]
    write_data(output_filename, result_data)

    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")