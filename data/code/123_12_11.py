def validate_input(input_tuple):
    if not isinstance(input_tuple, tuple):
        raise ValueError("Input must be a tuple")
    for item in input_tuple:
        if not isinstance(item, float):
            raise TypeError("All elements of the tuple must be floats")

def sum_tuple_elements(float_tuple):
    validate_input(float_tuple)
    return sum(float_tuple)

if __name__ == '__main__':
    sample_tuple = (3.5, 2.1, 4.8)
    result = sum_tuple_elements(sample_tuple)
    print(f"Sum of {sample_tuple}: {result}")