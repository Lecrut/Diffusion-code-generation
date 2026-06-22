def run_length_encode(s):
    if not s:
        return ""
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = s[i]
            count = 1
    
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    
    return ''.join(encoded)

if __name__ == '__main__':
    sample1 = "aabbbcccc"
    print(run_length_encode(sample1))
    
    sample2 = "abc"
    print(run_length_encode(sample2))
    
    sample3 = "aaaaa"
    print(run_length_encode(sample3))
    
    sample4 = ""
    print(run_length_encode(sample4))
    
    sample5 = "a"
    print(run_length_encode(sample5))