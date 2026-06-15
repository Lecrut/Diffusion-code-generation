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
    except Exception as e:
        print(f"An unexpected error occurred during file reading: {e}")
        sys.exit(1)
    if not numbers:
        print("No numerical data found in the file.")
        return
    average = sum(numbers) / len(numbers)
    print(f"The average of the numbers is: {average}")
if __name__ == '__main__':
    sample_filename = "data.txt"
    try:
        with open(sample_filename, 'w') as f:
            f.write("10.5\n")
            f.write("20\n")
            f.write("3.5\n")
            f.write("error_line\n")
            f.write("40\n")
        calculate_average(sample_filename)
    except Exception as e:
        print(f"An error occurred during setup or execution: {e}")