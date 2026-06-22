def sort_integers_in_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            line = file.read().strip()
            numbers = list(map(int, line.split()))
        numbers.sort()
        with open(output_filename, 'w') as file:
            file.write(' '.join(map(str, numbers)))
    except FileNotFoundError:
        print(f'Error: The file {input_filename} does not exist.')
    except ValueError:
        print('Error: The file contains non-integer values.')
    except IOError:
        print('An error occurred while reading or writing the file.')
if __name__ == '__main__':
    input_data = '3 1 4 1 5 9 2 6 5 3 5'
    output_filename = 'sorted_numbers.txt'
    with open('temp_input.txt', 'w') as temp_file:
        temp_file.write(input_data)
    sort_integers_in_file('temp_input.txt', output_filename)
    with open(output_filename, 'r') as result_file:
        sorted_numbers = result_file.read().strip()
        print(sorted_numbers)