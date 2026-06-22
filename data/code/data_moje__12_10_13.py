def get_middle_element(data):
    if not data:
        return None
    return data[len(data) // 2]

if __name__ == '__main__':
    test_cases = [[1, 2, 3, 4, 5], [10, 20], [], [42]]
    for case in test_cases:
        result = get_middle_element(case)
        print(result)