def test_or_condition():
    sample_values = [
        (True, False),
        (False, True),
        (True, True),
        (False, False),
    ]
    results = []
    for a, b in sample_values:
        result = a or b
        results.append(result)
    return results

if __name__ == '__main__':
    print(test_or_condition())