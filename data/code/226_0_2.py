def repeat_elements(sequence, repetitions):
    result = []
    for element in sequence:
        for _ in range(repetitions):
            result.append(element)
    return result

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    repeated_sequence = repeat_elements(sample_sequence, 10)
    print(repeated_sequence)