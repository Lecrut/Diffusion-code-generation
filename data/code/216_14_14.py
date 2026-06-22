def find_central_element(sequence):
    length = len(sequence)
    if length % 2 == 0:
        raise ValueError("Sequence has an even number of elements")
    central_index = length // 2
    return sequence[central_index]

if __name__ == '__main__':
    sample_sequence = [7, 3, 1, 8, 4, 9]
    try:
        print(find_central_element(sample_sequence))
    except ValueError as e:
        print(e)