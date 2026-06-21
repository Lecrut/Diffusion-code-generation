def run_length_encode(s):
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = s[i]
            count = 1
    
    result.append(str(count))
    result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    sample1 = "aabcccccaaa"
    print(run_length_encode(sample1))
    
    sample2 = "abcdef"
    print(run_length_encode(sample2))
    
    sample3 = "aabbcc"
    print(run_length_encode(sample3))
    
    sample4 = ""
    print(run_length_encode(sample4))
    
    sample5 = "aaaaa"
    print(run_length_encode(sample5))