def get_middle_value(items):
    length = len(items)
    if length == 0:
        return None
    index = length // 2
    if length % 2 == 0:
        return items[index - 1]
    return items[index]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        [7],
        [],
        [5, 1, 9, 3, 8]
    ]
    for case in test_cases:
        result = get_middle_value(case)
        print(f"List: {case} -> Middle: {result}")