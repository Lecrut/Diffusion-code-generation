def find_middle_element(sequence):
    n = len(sequence)
    if n == 0:
        return None
    middle_index = n // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_lists = {
        'odd': [1, 3, 5, 7, 9],
        'even': [2, 4, 6, 8, 10, 12],
        'single': [42],
        'empty': []
    }
    
    for key, lst in sample_lists.items():
        result = find_middle_element(lst)
        print(f"Middle element of {key} list: {result}")