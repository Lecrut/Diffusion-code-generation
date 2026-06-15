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
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    return numbers
if __name__ == '__main__':
    sample_filename = "data.txt"
    try:
        with open(sample_filename, 'w') as f:
            f.write("10\n")
            f.write("20.5\n")
            f.write("30\n")
            f.write("invalid_data\n")
            f.write("-5\n")
        numbers = calculate_average(sample_filename)
        if numbers:
            average = sum(numbers) / len(numbers)
            print(f"The average of the numbers in {sample_filename} is: {average}")
        else:
            print(f"No valid numbers found in {sample_filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")