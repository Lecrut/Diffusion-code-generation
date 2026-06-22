def validate_input(input_list):
    if not all(isinstance(item, int) for item in input_list):
        raise ValueError("All elements in the list must be integers")

def print_integers(integer_list):
    index = 0
    while index < len(integer_list):
        print(integer_list[index])
        index += 1

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    validate_input(sample_values)
    print_integers(sample_values)