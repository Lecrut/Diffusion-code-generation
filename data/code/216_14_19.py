def find_central_element(sequence):
    length = len(sequence)
    if length % 2 == 0:
        return None
    else:
        return sequence[length // 2]

if __name__ == '__main__':
    sample_sequence = [7, 3, 1, 8, 4, 9]
    print(find_central_element(sample_sequence))