def repeat_elements(input_tuple):
    if not all(isinstance(item, int) for item in input_tuple):
        raise ValueError("All elements must be integers")
    return [item for item in input_tuple for _ in range(5)]

if __name__ == '__main__':
    sample_input = (1, 2, 3)
    try:
        result = repeat_elements(sample_input)
        print(result)
    except ValueError as e:
        print(e)