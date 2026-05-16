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
        print(f"Error reading file: {e}")
        return None
    return has_positive
if __name__ == '__main__':
    sample_filename = "numbers.txt"
    with open(sample_filename, 'w') as f:
        f.write("10\n")
        f.write("-5\n")
        f.write("0\n")
        f.write("22\n")
    result = check_for_positive(sample_filename)
    if result is not None:
        if result:
            print("At least one number in the list is positive.")
        else:
            print("No positive numbers found in the list.")