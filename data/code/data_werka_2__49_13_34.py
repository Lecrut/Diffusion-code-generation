def compare_lengths_within_threshold(length1: int, length2: int, threshold: int) -> bool:
    return abs(length1 - length2) <= threshold

if __name__ == '__main__':
    test_cases = [
        {'length1': 100, 'length2': 105, 'threshold': 5},
        {'length1': 200, 'length2': 210, 'threshold': 8},
        {'length1': 300, 'length2': 295, 'threshold': 10}
    ]
    
    for case in test_cases:
        result = compare_lengths_within_threshold(case['length1'], case['length2'], case['threshold'])
        print(f"Lengths: {case['length1']}, {case['length2']} with Threshold {case['threshold']}: {result}")