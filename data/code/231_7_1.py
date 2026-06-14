def repeating_sequence_generator(sequence):
    n = len(sequence)
    while True:
        for i in range(n):
            yield sequence[i]
if __name__ == '__main__':
    pattern = [1, 2, 3, 4]
    generator = repeating_sequence_generator(pattern)
    print("Repeating sequence of [1, 2, 3, 4]:")
    for i in range(10):
        result = []
        for _ in range(4):
            result.append(next(generator))
        print(result)