def get_penultimate_element(data):
    if len(data) < 2:
        return None
    return data[-2]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20],
        [5],
        [],
        ['a', 'b', 'c']
    ]
    for case in test_cases:
        print(get_penultimate_element(case))