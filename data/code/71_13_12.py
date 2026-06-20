def find_middle_element(data_list):
    n = len(data_list)
    if n == 0:
        return None
    middle_index = n // 2
    return data_list[middle_index]

if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4, 5], 3),
        ([10, 20, 30, 40], 30),
        ([99], 99),
        ([], None)
    ]
    
    for i, (lst, expected) in enumerate(test_cases):
        result = find_middle_element(lst)
        print(f"Test case {i+1}: List {lst} -> Expected: {expected}, Got: {result}")