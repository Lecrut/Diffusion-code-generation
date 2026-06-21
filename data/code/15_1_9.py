PENULTIMATE_INDEX = -2
MINIMUM_LENGTH = 2

def get_penultimate_value(sequence):
    if len(sequence) < MINIMUM_LENGTH:
        raise ValueError("Sequence requires at least two items")
    return sequence[PENULTIMATE_INDEX]

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    computed_value = get_penultimate_value(sample_data)
    print(computed_value)
    
    minimal_data = [42, 43]
    minimal_result = get_penultimate_value(minimal_data)
    print(minimal_result)