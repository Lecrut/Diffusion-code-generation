def run_length_encode(data):
    if not data:
        return {}
    
    counts = {}
    i = 0
    n = len(data)
    
    while i < n:
        current_char = data[i]
        count = 1
        while i + 1 < n and data[i + 1] == current_char:
            count += 1
            i += 1
        counts[current_char] = count
        i += 1
        
    return counts

if __name__ == '__main__':
    test_cases = [
        "aaabbc",
        "aabcc",
        "abcde",
        "a",
        ""
    ]
    
    all_results = {}
    for case in test_cases:
        result = run_length_encode(case)
        all_results[case] = result
        
    print(all_results)