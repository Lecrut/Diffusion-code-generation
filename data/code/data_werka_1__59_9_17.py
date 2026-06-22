def find_middle_item(sequence):
    if not sequence:
        return None
    middle_index = len(sequence) // 2
    return sequence[middle_index]

if __name__ == '__main__':
    SAMPLE_INPUT = [1, 3, 5, 7, 9]
    result = find_middle_item(SAMPLE_INPUT)
    print(result)