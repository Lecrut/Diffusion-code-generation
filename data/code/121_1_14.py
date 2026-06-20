def compare_floats(a: float, b: float) -> str:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both inputs must be numbers.')
    if abs(a - b) < 1e-09:
        return 'equal'
    elif a > b:
        return 'first_greater'
    else:
        return 'second_greater'
if __name__ == '__main__':
    sample1 = compare_floats(0.1 + 0.2, 0.3)
    print(sample1)
    sample2 = compare_floats(1.1, 1.2)
    print(sample2)