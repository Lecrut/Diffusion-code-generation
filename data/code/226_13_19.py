if __name__ == '__main__':
    sequence = [1, 2, 3]
    num_repeats = 5
    full_sequence = [item for _ in range(num_repeats) for item in sequence]
    print(full_sequence)