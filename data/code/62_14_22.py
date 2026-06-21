def retrieve_second(lst):
    if len(lst) < 2:
        return None
    return lst[1]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4],
        ['x', 'y'],
        [True],
        [],
        [9, 8, 7]
    ]
    for i, case in enumerate(test_cases):
        print(f"Test Case {i+1}: {retrieve_second(case)}")