def repeat_lines(file_path, output_file_path, Q):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    repeated_lines = [line.strip() for line in lines] * Q
    
    with open(output_file_path, 'w') as file:
        file.writelines(repeated_lines)

if __name__ == '__main__':
    input_file = 'sample.txt'
    output_file = 'output.txt'
    Q = 3
    repeat_lines(input_file, output_file, Q)
    print(f"Lines repeated {Q} times and written to {output_file}")