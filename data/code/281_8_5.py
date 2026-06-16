def calculate_total(filename):
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
            f.write("30\n")
            f.write("invalid_number\n")
            f.write("-5\n")
        result = calculate_total(file_name)
        if result is not None:
            print(f"The grand total sum is: {result}")
    except Exception as e:
        print(f"An unexpected error occurred during setup or execution: {e}")