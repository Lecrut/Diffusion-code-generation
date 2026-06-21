def encode_string(input_string):
    if not input_string:
        return []
    
    result = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = input_string[i]
            count = 1
    
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    test_cases = [
        "aabbbcdddd",
        "a",
        "",
        "aabbcc",
        "aaabbbcccc",
        "11223334444"
    ]
    
    for test in test_cases:
        encoded = encode_string(test)
        print(f"Input: '{test}' -> Output: {encoded}")