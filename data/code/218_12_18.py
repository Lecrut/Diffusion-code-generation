def parse_input(input_line):
    try:
        numbers = [int(x) for x in input_line.split()]
        if not numbers:
            raise ValueError('Input is empty or contains no valid integers.')
        return numbers
    except ValueError as e:
        print(f'Error: {e}')
        return None

def find_smallest(numbers):
    if not numbers:
        return None
    return min(numbers)
if __name__ == '__main__':
    sample_input = '10 5 -3 8 2'
    parsed_numbers = parse_input(sample_input)
    smallest_value = find_smallest(parsed_numbers)
    print(smallest_value)