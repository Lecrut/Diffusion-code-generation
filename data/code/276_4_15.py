def repeat_lines(input_file, output_file, Q):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
    
    repeated_lines = [line.strip() for line in lines] * Q
    
    with open(output_file, 'w') as outfile:
        outfile.writelines(f"{line}\n" for line in repeated_lines)

if __name__ == '__main__':
    repeat_lines('sample.txt', 'output.txt', 3)