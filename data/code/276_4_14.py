def repeat_lines(input_file_path, output_file_path, q):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    repeated_lines = [line.strip() for line in lines] * q

    with open(output_file_path, 'w') as output_file:
        output_file.writelines(f"{line}\n" for line in repeated_lines)

if __name__ == '__main__':
    sample_input_file_path = 'sample.txt'
    sample_output_file_path = 'output.txt'
    Q = 3

    repeat_lines(sample_input_file_path, sample_output_file_path, Q)