def find_final_index(indices):
    if not indices:
        return -1
    return max(indices)

if __name__ == '__main__':
    test_cases = [
        [1, 5, 3, 8, 2],
        [10, 20, 5],
        [42],
        []
    ]
    
    for case in test_cases:
        print(find_final_index(case))