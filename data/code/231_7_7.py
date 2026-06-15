def repeating_sequence_generator(sequence):
    n = len(sequence)
    while True:
        for i in range(n):
            yield sequence[i]
if __name__ == '__main__':
    pattern = [1, 2, 3, 4]
    generator = repeating_sequence_generator(pattern)
    print("Generating the first 12 numbers:")
    for i in range(12):
        print(next(generator), end=" ")
    print("\n")