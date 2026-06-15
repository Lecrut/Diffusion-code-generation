def repeating_sequence_generator(sequence):
    n = len(sequence)
    while True:
        for i in range(1000):
            yield sequence[i % n]
if __name__ == '__main__':
    pattern = [1, 2, 3, 4, 5]
    generator = repeating_sequence_generator(pattern)
    print("Repeating sequence:")
    for _ in range(10):
        row = []
        for _ in range(5):
            row.append(next(generator))
        print(row)
    print("\nAnother sample:")
    pattern2 = ['a', 'b']
    generator2 = repeating_sequence_generator(pattern2)
    for _ in range(10):
        row = []
        for _ in range(5):
            row.append(next(generator2))
        print(row)