numbers = [1, 2, 3, 4, 5]

def repeat_elements(sequence, repetitions):
    if not all(isinstance(x, int) for x in sequence):
        raise ValueError("All elements in the sequence must be integers.")
    if not isinstance(repetitions, int) or repetitions < 0:
        raise ValueError("Repetitions must be a non-negative integer.")
    
    result = []
    for element in sequence:
        result.extend([element] * repetitions)
    return result

if __name__ == '__main__':
    repeated_sequence = repeat_elements(numbers, 10)
    print(repeated_sequence)