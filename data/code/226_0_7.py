NUMBERS = [1, 2, 3, 4, 5]
REPEAT_COUNT = 10

def repeat_elements(sequence, repetitions):
    result = []
    for element in sequence:
        for _ in range(repetitions):
            result.append(element)
    return result

if __name__ == '__main__':
    repeated_sequence = repeat_elements(NUMBERS, REPEAT_COUNT)
    print(repeated_sequence)