def find_middle_item(sequence):
    if not sequence:
        return None
    n = len(sequence)
    middle_index = n // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    result = find_middle_item(sample_sequence)
    print(result)