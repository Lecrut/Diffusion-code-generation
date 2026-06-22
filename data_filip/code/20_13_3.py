def run_length_encode(input_string: str) -> list:
    if not input_string:
        return []
    
    result = []
    count = 1
    current_char = input_string[0]
    
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
    test_strings = [
        "AAABBBCCDAA",
        "",
        "A",
        "AAAAA",
        "ABC"
    ]
    
    for s in test_strings:
        encoded = run_length_encode(s)
        print(encoded)