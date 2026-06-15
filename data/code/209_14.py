import os
def calculate_average(filename):
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    stripped_line = line.strip()
                    if stripped_line:
                        number = float(stripped_line)
                        numbers.append(number)
                except ValueError:
                    print(f"Error: Skipping non-numeric data found on line: {line.strip()}")
                except Exception as e:
                    print(f"An unexpected error occurred while processing a line: {line.strip()}. Error: {e}")
        if not numbers:
            return None
        else:
            return sum(numbers) / len(numbers)
    except FileNotFoundError:
        print(f"Error: File not found at {filename}")
        return None
    except IOError as e:
        print(f"Error reading file {filename}: {e}")
        return None
if __name__ == '__main__':
    test_filename = "sample_data.txt"
    try:
        with open(test_filename, 'w') as f:
            f.write("10.5\n")
            f.write("20\n")
            f.write("3.14\n")
            f.write("invalid_data\n")
            f.write("40\n")
            f.write("\n")
            f.write("-5.5\n")
        average = calculate_average(test_filename)
        if average is not None:
            print(f"The calculated average is: {average}")
        else:
            print("Could not calculate the average.")
    except Exception as e:
        print(f"An error occurred during setup or execution: {e}")
    finally:
        if os.path.exists(test_filename):
            os.remove(test_filename)