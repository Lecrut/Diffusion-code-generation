def find_largest_number(filename):
    try:
        with open(filename, 'r') as file:
            numbers = []
            for line in file:
                try:
                    number = float(line.strip())
                    numbers.append(number)
                except ValueError:
                    continue
            if not numbers:
                return None
            return max(numbers)
    except FileNotFoundError:
        return None
    except Exception:
        return None
if __name__ == '__main__':
    sample_filename = "numbers.txt"
    with open(sample_filename, 'w') as f:
        f.write("10\n")
        f.write("5\n")
        f.write("42\n")
        f.write("99\n")
        f.write("3\n")
    largest = find_largest_number(sample_filename)
    if largest is not None:
        print(largest)
    else:
        print("Error reading file or no numbers found.")