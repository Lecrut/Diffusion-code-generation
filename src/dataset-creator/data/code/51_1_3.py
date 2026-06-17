def get_first_item(items):
    if not items:
        return None
    return items[0]
if __name__ == '__main__':
    test_cases = [
        ['apple', 'banana'],
        [],
        [1, 2, 3],
        ['single']
    ]
    for i, case in enumerate(test_cases):
        result = get_first_item(case)
        print(f"Input: {case}, Output: {result}")