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
    except IOError:
        print(f"Error: Could not read file '{filename}'.")
        return None
    if not numbers:
        return 0.0
    else:
        return sum(numbers) / len(numbers)
if __name__ == '__main__':
    file_name = 'data.txt'
    try:
        with open(file_name, 'w') as f:
            f.write("10\n")
            f.write("20\n")
            f.write("30\n")
            f.write("40\n")
            f.write("error_line\n")
            f.write("50\n")
        average = calculate_average(file_name)
        if average is not None:
            print(f"The average of the numbers in '{file_name}' is: {average}")
    except Exception as e:
        print(f"An unexpected error occurred during file setup or execution: {e}")