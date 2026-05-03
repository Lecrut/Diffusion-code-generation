import os
input_filename = "input.txt"
output_filename = "output.txt"
sample_content = "5 2 8 1 9 3"
try:
    with open(input_filename, 'w') as f:
        f.write(sample_content)
except IOError as e:
    print(f"Error writing to {input_filename}: {e}")
    exit(1)
try:
    with open(input_filename, 'r') as infile:
        content = infile.read().strip()
        if not content:
            print("Input file is empty.")
            exit(1)
        numbers = list(map(int, content.split()))
        sorted_numbers = sorted(numbers)
        with open(output_filename, 'w') as outfile:
            output_content = " ".join(map(str, sorted_numbers))
            outfile.write(output_content + "\n")
except FileNotFoundError:
    print(f"Error: Input file {input_filename} not found.")
    exit(1)
except ValueError:
    print(f"Error: Could not convert all parts of the input to integers.")
    exit(1)
except IOError as e:
    print(f"Error during file operation: {e}")
    exit(1)
if __name__ == '__main__':
    pass