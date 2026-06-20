def find_middle_element(lst):
    return lst[len(lst) // 2 - 1] if len(lst) % 2 == 0 else lst[len(lst) // 2]

if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4], 2),
        ([7], 7),
        ([], None),
        ([9, 8, 7, 6, 5, 4, 3, 2, 1], 5)
    ]

    for i, (lst, expected) in enumerate(test_cases):
        result = find_middle_element(lst)
        print(f"Test case {i+1}: {'Pass' if result == expected else 'Fail'}")