def sort_integers_in_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            line = file.readline().strip()
            numbers = list(map(int, line.split()))
        numbers.sort()
        with open(output_filename, 'w') as file:
            file.write(' '.join(map(str, numbers)))
    except FileNotFoundError:
        print('The input file was not found.')
    except ValueError:
        print('The file contains non-integer values.')
    except Exception as e:
        print(f'An error occurred: {e}')
if __name__ == '__main__':
    sample_input = 'input.txt'
    sample_output = 'output.txt'
    with open(sample_input, 'w') as file:
        file.write('3 1 4 1 5 9 2 6 5 3 5')
    sort_integers_in_file(sample_input, sample_output)