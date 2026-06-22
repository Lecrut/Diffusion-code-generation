def run_length_encode(data):
    if not data:
        return ""
    
    encoded = []
    count = 1
    prev_char = data[0]
    
    for i in range(1, len(data)):
        current_char = data[i]
        if current_char == prev_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count) + prev_char)
            else:
                encoded.append(prev_char)
            count = 1
            prev_char = current_char
    
    if count > 1:
        encoded.append(str(count) + prev_char)
    else:
        encoded.append(prev_char)
    
    return "".join(encoded)

if __name__ == '__main__':
    test_strings = ["AABCCCCCAAD", "XYZ", "AAAA", "a"]
    results = {}
    
    for s in test_strings:
        result = run_length_encode(s)
        results[s] = result
        print(result)