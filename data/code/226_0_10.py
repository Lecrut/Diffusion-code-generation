def repeat_elements(sequence):
    if not isinstance(sequence, list) or not all(isinstance(x, int) for x in sequence):
        raise ValueError("Input must be a list of integers")
    
    result = []
    for element in sequence:
        result.extend([element] * 10)
    return result

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    repeated_sequence = repeat_elements(sample_sequence)
    print(repeated_sequence)