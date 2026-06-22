def get_penultimate(lst):
    if len(lst) < 2:
        return None
    return lst[-2]

if __name__ == '__main__':
    test_cases = [[1, 2, 3], [10], [], [5, 6], [100, 200, 300, 400]]
    for case in test_cases:
        print(get_penultimate(case))