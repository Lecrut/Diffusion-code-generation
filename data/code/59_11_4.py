def find_middle_element(sequence):
    if not sequence:
        return None
    middle_index = len(sequence) // 2
    return sequence[middle_index]
if __name__ == '__main__':
    sample_lists = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10, 12], [42], []]
    for lst in sample_lists:
        result = find_middle_element(lst)
        print(f'Middle element of {lst}: {result}')