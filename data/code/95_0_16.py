def analyze_properties(value):
    results = dict()
    results['is_positive'] = value > 0
    results['is_even'] = value % 2 == 0
    results['is_div_by_3'] = value % 3 == 0
    return results

if __name__ == '__main__':
    test_cases = [12, -3, 7, 0, 15]
    for val in test_cases:
        props = analyze_properties(val)
        print(f"{val}: {props}")