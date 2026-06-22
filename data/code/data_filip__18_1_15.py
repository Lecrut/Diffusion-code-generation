def run_length_encoding(s):
    if not s:
        return []
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = s[i]
            count = 1
    
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_input = "AAABBBCCDEEEE"
    encoded_result = run_length_encoding(sample_input)
    print(encoded_result)