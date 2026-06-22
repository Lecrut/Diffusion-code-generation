def _validate_non_empty_sequence(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    if len(sequence) == 0:
        raise ValueError("Sequence must contain at least one element")

def retrieve_boundary_elements(sequence):
    _validate_non_empty_sequence(sequence)
    return (sequence[0], sequence[-1])

if __name__ == '__main__':
    sample_data = [42, 17, 99, 8, 3]
    output = retrieve_boundary_elements(sample_data)
    print(output)