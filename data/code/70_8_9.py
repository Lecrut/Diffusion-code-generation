def check_first_last(sequence):
    if sequence:
        return sequence[0], sequence[-1]
    return None, None

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    first, last = check_first_last(sample_sequence)
    print(f"First: {first}, Last: {last}")