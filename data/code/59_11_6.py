def find_middle_element(sequence):
    n = len(sequence)
    if n == 0:
        return None
    middle_index = n // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_lists = {
        'odd': [7, 5, 3, 1],
        'even': [8, 6, 4, 2],
        'single': [42],
        'empty': []
    }
    for key, lst in sample_lists.items():
        result = find_middle_element(lst)
        print(f"Middle element of {key} list: {result}")