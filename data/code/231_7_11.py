import numpy as np

def repeating_sequence_generator(sequence):
    n = len(sequence)
    while True:
        for i in range(n):
            yield sequence[i]

if __name__ == '__main__':
    pattern = [True, False]
    generator = repeating_sequence_generator(pattern)
    print("Repeating boolean sequence:")
    for _ in range(25):
        row = []
        for _ in range(10):
            row.append(next(generator))
        print(row)