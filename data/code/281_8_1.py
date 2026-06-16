def calculate_file_sum(filename):
    total_sum = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    total_sum += number
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")
        return None
    return total_sum
if __name__ == '__main__':
    sample_filename = 'data.txt'
    try:
        with open(sample_filename, 'w') as f:
            f.write("10\n")
            f.write("25.5\n")
            f.write("-5\n")
            f.write("100\n")
            f.write("invalid_number\n")
            f.write("3.14\n")
        result = calculate_file_sum(sample_filename)
        if result is not None:
            print(result)
    except IOError as e:
        print(f"An error occurred during file setup or operation: {e}")