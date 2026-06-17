def calculate_sum_from_file(filename):
    total = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    total += number
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
        return total
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")
        return None
if __name__ == '__main__':
    file_name = 'data.txt'
    try:
        with open(file_name, 'w') as f:
            f.write("10\n")
            f.write("25.5\n")
            f.write("-5\n")
            f.write("100\n")
            f.write("invalid_number\n")
            f.write("3.14\n")
        result = calculate_sum_from_file(file_name)
        if result is not None:
            print(result)
    except IOError as e:
        print(f"An error occurred during file setup or operation: {e}")