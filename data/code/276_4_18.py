def repeat_lines(input_file, output_file, Q):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
    
    repeated_lines = [line.strip() for line in lines] * Q
    
    with open(output_file, 'w') as outfile:
        outfile.writelines('\n'.join(repeated_lines))

if __name__ == '__main__':
    input_file = 'sample.txt'
    output_file = 'output.txt'
    Q = 3
    repeat_lines(input_file, output_file, Q)
    print(f"Lines repeated {Q} times and written to {output_file}")