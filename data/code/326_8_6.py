def calculate_average(filename):
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    numbers.append(number)
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")
        return None
    if not numbers:
        return 0.0
    else:
        average = sum(numbers) / len(numbers)
        return average
if __name__ == '__main__':
    file_name = 'data.txt'
    try:
        with open(file_name, 'w') as f:
            f.write("10\n")
            f.write("20\n")
            f.write("30.5\n")
            f.write("40\n")
    except IOError as e:
        print(f"Error writing sample data: {e}")
    average_result = calculate_average(file_name)
    if average_result is not None:
        print(average_result)