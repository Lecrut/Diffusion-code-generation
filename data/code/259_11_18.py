def find_min_max(data):
    if not data:
        raise ValueError("Input list is empty")
    return min(data), max(data)

def process_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            data = [int(line.strip()) for line in file]
            minimum, maximum = find_min_max(data)
        with open(output_file, 'w') as file:
            file.write(f"Minimum: {minimum}\nMaximum: {maximum}")
    except FileNotFoundError:
        print(f"The file '{input_file}' does not exist.")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    input_list = [3, 1, 4, 1, 5, 9, 2, 6]
    process_file('input.txt', 'output.txt')