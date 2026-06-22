def retrieve_second_element(lst):
    if len(lst) < 2:
        return None
    return lst[1]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4],
        ['a', 'b'],
        [True],
        [],
        [99, 88]
    ]
    for i, case in enumerate(test_cases):
        print(f"Test Case {i + 1}: {retrieve_second_element(case)}")