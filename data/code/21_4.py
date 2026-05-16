import os
input_filename = "input.txt"
output_filename = "output.txt"
sample_data = "5 2 8 1 9 4"
try:
    with open(input_filename, 'w') as f:
        f.write(sample_data + "\n")
except IOError as e:
    print(f"Error writing to {input_filename}: {e}")
    exit()
try:
    with open(input_filename, 'r') as infile:
        content = infile.read().strip()
        if not content:
            print("Input file is empty.")
            exit()
        numbers = list(map(int, content.split()))
        sorted_numbers = sorted(numbers)
        with open(output_filename, 'w') as outfile:
            for num in sorted_numbers:
                outfile.write(str(num) + "\n")
except FileNotFoundError:
    print(f"Error: Input file {input_filename} not found.")
except ValueError:
    print(f"Error: Could not convert all input to integers in {input_filename}.")
except IOError as e:
    print(f"Error during file operation: {e}")
if __name__ == '__main__':
    pass