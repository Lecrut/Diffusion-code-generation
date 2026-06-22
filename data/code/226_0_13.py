numbers = [1, 2, 3, 4, 5]

def repeat_elements(sequence, repetitions):
    result = []
    for element in sequence:
        result.extend([element] * repetitions)
    return result

if __name__ == '__main__':
    repeated_sequence = repeat_elements(numbers, 10)
    print(repeated_sequence)