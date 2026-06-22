def sort_integers_from_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            line = file.readline().strip()
            numbers = list(map(int, line.split()))
        numbers.sort()
        with open(output_filename, 'w') as file:
            file.write(' '.join(map(str, numbers)))
    except FileNotFoundError:
        print(f'Error: The file {input_filename} does not exist.')
    except IOError:
        print(f'Error: An I/O error occurred while reading or writing files.')
if __name__ == '__main__':
    input_data = '3 1 4 1 5 9 2 6 5 3 5'
    input_filename = 'input.txt'
    output_filename = 'output.txt'
    with open(input_filename, 'w') as file:
        file.write(input_data)
    sort_integers_from_file(input_filename, output_filename)
    with open(output_filename, 'r') as file:
        sorted_numbers = file.readline().strip()
    print(sorted_numbers)