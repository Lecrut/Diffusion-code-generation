sequence = [1, 2, 3, 4, 5]
repetitions = 10

def repeat_sequence(sequence, repetitions):
    result = []
    for number in sequence:
        result.extend([number] * repetitions)
    return result

if __name__ == '__main__':
    output = repeat_sequence(sequence, repetitions)
    print(output)