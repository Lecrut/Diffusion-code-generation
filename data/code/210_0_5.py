import os
def find_min_max(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    continue
    except IOError as e:
        raise IOError(f"Error reading file: {e}")
    if not numbers:
        return None, None
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum
if __name__ == '__main__':
    sample_filename = "numbers.txt"
    sample_data = [10, 5, 22, 8, 30, 1]
    try:
        with open(sample_filename, 'w') as f:
            for num in sample_data:
                f.write(str(num) + '\n')
        minimum_val, maximum_val = find_min_max(sample_filename)
        if minimum_val is not None and maximum_val is not None:
            print(f"Minimum value: {minimum_val}")
            print(f"Maximum value: {maximum_val}")
        else:
            print("No valid numbers found in the file.")
    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(f"An I/O error occurred: {e}")