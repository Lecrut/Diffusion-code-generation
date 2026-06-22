def flatten_sequence(input_tuple):
    if not all(isinstance(num, int) for num in input_tuple):
        raise ValueError("All elements in the tuple must be integers.")
    
    return [num for num in input_tuple for _ in range(5)]

if __name__ == '__main__':
    sample_input = (1, 2, 3)
    try:
        result = flatten_sequence(sample_input)
        print(result)
    except ValueError as e:
        print(e)