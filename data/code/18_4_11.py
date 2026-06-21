def get_middle_value(values):
    length = len(values)
    if length == 0:
        return None
    return values[length // 2]

if __name__ == '__main__':
    test_cases = [
        [10, 20, 30, 40, 50],
        [5, 15, 25],
        [100],
        [1, 2, 3, 4],
        []
    ]
    for case in test_cases:
        result = get_middle_value(case)
        print(f"List: {case}, Middle: {result}")