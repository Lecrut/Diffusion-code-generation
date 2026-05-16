def check_for_positive(filename):
    has_positive = False
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    if number > 0:
                        has_positive = True
                        break
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")
        return None
    return has_positive
if __name__ == '__main__':
    sample_filename = "numbers.txt"
    try:
        with open(sample_filename, 'w') as f:
            f.write("10\n")
            f.write("-5\n")
            f.write("0\n")
            f.write("22\n")
            f.write("-1\n")
        result = check_for_positive(sample_filename)
        if result is not None:
            print(f"Does the list contain at least one positive number? {result}")
    except IOError as e:
        print(f"An error occurred during file setup: {e}")