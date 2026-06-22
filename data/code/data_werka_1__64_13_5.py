def find_final_index(indices):
    if not indices:
        return -1
    return max(indices)

if __name__ == '__main__':
    test_cases = {
        'case1': [1, 5, 3, 8, 2],
        'case2': [10, 20, 5],
        'case3': [42],
        'case4': [],
        'case5': [7, 3, 9, 3, 9]
    }
    
    for name, indices in test_cases.items():
        result = find_final_index(indices)
        print(f"{name}: {result}")