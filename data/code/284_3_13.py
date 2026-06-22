def reverse_integers_in_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        integers = [int(line.strip()) for line in input_file]
    
    reversed_integers = list(reversed(integers))
    
    with open(output_file_path, 'w') as output_file:
        for number in reversed_integers:
            output_file.write(f"{number}\n")

if __name__ == '__main__':
    sample_input_file_path = 'sample_input.txt'
    sample_output_file_path = 'sample_output.txt'
    
    with open(sample_input_file_path, 'w') as file:
        file.write("1\n2\n3\n4\n5\n")
    
    reverse_integers_in_file(sample_input_file_path, sample_output_file_path)
    
    with open(sample_output_file_path, 'r') as file:
        print(file.read())