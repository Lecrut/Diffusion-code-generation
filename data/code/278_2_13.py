def validate_input(items):
    if not all(isinstance(item, int) for item in items):
        raise ValueError("All elements must be integers")

def print_integers(integer_list):
    validate_input(integer_list)
    index = 0
    while index < len(integer_list):
        print(integer_list[index])
        index += 1

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print_integers(sample_values)