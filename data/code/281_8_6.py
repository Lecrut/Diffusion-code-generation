def calculate_total(filename):
    total = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    total += number
                except ValueError:
                    print(f"Skipping non-numeric line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    return total
if __name__ == '__main__':
    file_name = 'data.txt'
    try:
        with open(file_name, 'w') as f:
            f.write("10\n")
            f.write("25.5\n")
            f.write("-5\n")
            f.write("100\n")
            f.write("invalid_line\n")
        grand_total = calculate_total(file_name)
        if grand_total is not None:
            print(f"The grand total sum of numbers in {file_name} is: {grand_total}")
    except IOError as e:
        print(f"An error occurred during file operation: {e}")