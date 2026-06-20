def validate_input(input_tuple):
    if not isinstance(input_tuple, tuple) or not all(isinstance(item, float) for item in input_tuple):
        raise ValueError("Input must be a tuple of floats")

def sum_tuple_elements(float_tuple):
    validate_input(float_tuple)
    return sum(float_tuple)

if __name__ == '__main__':
    sample_tuple = (3.5, 2.1, 4.8)
    print(sum_tuple_elements(sample_tuple))