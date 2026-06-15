def repeat_sequence():
    sequence = list(range(1, 6))
    repetitions = 10
    result = []
    for _ in range(repetitions):
        result.extend(sequence)
    return result
if __name__ == '__main__':
    output = repeat_sequence()
    print(output)