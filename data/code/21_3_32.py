def sort_integers_from_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            line = file.readline().strip()
            integers = list(map(int, line.split()))
        integers.sort()
        with open(output_filename, 'w') as file:
            file.write(' '.join(map(str, integers)))
    except FileNotFoundError:
        print('Error: The input file was not found.')
    except ValueError:
        print('Error: The file contains non-integer values.')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
if __name__ == '__main__':
    sample_input = '3 1 4 1 5 9'
    sample_output_filename = 'sorted_integers.txt'
    with open('temp_input.txt', 'w') as temp_file:
        temp_file.write(sample_input)
    sort_integers_from_file('temp_input.txt', sample_output_filename)
    with open(sample_output_filename, 'r') as result_file:
        sorted_content = result_file.read().strip()
        print(sorted_content)