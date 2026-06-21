def run_length_encode(data):
    if not data:
        return {}

    counts = {}
    current_char = data[0]
    count = 1

    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            counts[current_char] = count
            current_char = data[i]
            count = 1

    counts[current_char] = count
    return counts

if __name__ == '__main__':
    test_cases = [
        'aabbc',
        'aaaabbbcc',
        'hello',
        'a',
        'xyz',
        ''
    ]

    results = {}
    for test in test_cases:
        key = f"input_{repr(test)}"
        results[key] = run_length_encode(test)

    print(results)