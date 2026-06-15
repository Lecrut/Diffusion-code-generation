import sys
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
        print(f"Error: File not found - {filename}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}", file=sys.stderr)
        return None
    if not numbers:
        return 0.0
    else:
        average = sum(numbers) / len(numbers)
        return average
if __name__ == '__main__':
    sample_filename = "data.txt"
    try:
        with open(sample_filename, 'w') as f:
            f.write("10\n")
            f.write("20.5\n")
            f.write("30\n")
            f.write("invalid_data\n")
            f.write("40\n")
        result = calculate_average(sample_filename)
        if result is not None:
            print(f"The average of the numbers in {sample_filename} is: {result}")
    except Exception as e:
        print(f"An error occurred during setup or execution: {e}", file=sys.stderr)