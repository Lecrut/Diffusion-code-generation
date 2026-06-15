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
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_filename = "data.txt"
    try:
        with open(sample_filename, 'w') as f:
            f.write("10\n")
            f.write("20\n")
            f.write("30\n")
            f.write("40\n")
            f.write("not_a_number\n")
            f.write("50\n")
        average = calculate_average(sample_filename)
        if average is not None:
            print(f"The average of the numbers in {sample_filename} is: {average}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)