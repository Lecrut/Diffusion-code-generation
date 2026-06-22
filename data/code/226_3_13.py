def validate_input(input_tuple):
    if not all(isinstance(item, int) for item in input_tuple):
        raise ValueError("All elements in the tuple must be integers")

def flatten_sequence(input_tuple):
    validate_input(input_tuple)
    return [num for num in input_tuple for _ in range(5)]

if __name__ == '__main__':
    sample_input = (1, 2, 3)
    print(flatten_sequence(sample_input))