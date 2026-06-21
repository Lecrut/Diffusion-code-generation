def run_length_encode(sequence):
    if not sequence:
        return {}
    
    counts = {}
    current_char = sequence[0]
    count = 1
    
    for i in range(1, len(sequence)):
        if sequence[i] == current_char:
            count += 1
        else:
            counts[current_char] = counts.get(current_char, 0) + count
            current_char = sequence[i]
            count = 1
    
    counts[current_char] = counts.get(current_char, 0) + count
    return counts

if __name__ == '__main__':
    test_cases = [
        "AAABBBCCDAA",
        "ABABABAB",
        "AAAAAA",
        "",
        "XYZXYZ",
        "112233344444"
    ]
    
    for test in test_cases:
        result = run_length_encode(test)
        print(result)