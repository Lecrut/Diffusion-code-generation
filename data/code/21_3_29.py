def sort_integers_from_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            line = file.readline().strip()
            integers = list(map(int, line.split()))
        integers.sort()
        with open(output_filename, 'w') as file:
            file.write(' '.join(map(str, integers)))
    except FileNotFoundError:
        print(f'Error: The file {input_filename} was not found.')
    except ValueError:
        print('Error: The file contains non-integer values.')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
if __name__ == '__main__':
    input_filename = 'sample_input.txt'
    output_filename = 'sorted_output.txt'
    with open(input_filename, 'w') as file:
        file.write('3 1 4 1 5 9 2 6 5 3 5')
    sort_integers_from_file(input_filename, output_filename)