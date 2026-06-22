def sort_integers_in_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            line = file.readline().strip()
            integers = list(map(int, line.split()))
        integers.sort()
        with open(output_filename, 'w') as file:
            file.write(' '.join(map(str, integers)))
    except FileNotFoundError:
        print('Error: The input file does not exist.')
    except ValueError:
        print('Error: The input file contains non-integer values.')
    except Exception as e:
        print(f'An error occurred: {e}')
if __name__ == '__main__':
    input_filename = 'input.txt'
    output_filename = 'output.txt'
    with open(input_filename, 'w') as file:
        file.write('3 1 4 1 5 9 2 6 5 3 5')
    sort_integers_in_file(input_filename, output_filename)
    with open(output_filename, 'r') as file:
        sorted_content = file.read().strip()
        print(sorted_content)