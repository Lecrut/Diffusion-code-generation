def run_length_encode(s):
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
    sample1 = "AAABBBCCD"
    print(run_length_encode(sample1))
    
    sample2 = "ABC"
    print(run_length_encode(sample2))
    
    sample3 = "AABBCC"
    print(run_length_encode(sample3))
    
    sample4 = ""
    print(run_length_encode(sample4))
    
    sample5 = "AAAAAAAAAA"
    print(run_length_encode(sample5))