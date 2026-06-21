def average(sequence):
    try:
        return sum(x for x in sequence) / len(sequence)
    except TypeError:
        raise ValueError("Input is not iterable")

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    print(average(sample_sequence))