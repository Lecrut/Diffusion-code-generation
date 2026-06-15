def calculate_absolute_difference(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            num1 = float(infile.read().strip())
            num2 = float(infile.readline().strip())
    except FileNotFoundError:
        print(f"Error: Input file {input_filename} not found.")
        return
    except ValueError:
        print(f"Error: Could not read valid numbers from {input_filename}.")
        return
    difference = abs(num1 - num2)
    with open(output_filename, 'w') as outfile:
        outfile.write(str(difference))
if __name__ == '__main__':
    input_file = "input.txt"
    output_file = "output.txt"
    with open(input_file, 'w') as f:
        f.write("15.5\n")
        f.write("8.2\n")
    calculate_absolute_difference(input_file, output_file)