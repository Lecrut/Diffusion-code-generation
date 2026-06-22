def run_length_encode(s):
    if not s:
        return ""
    
    encoded = []
    count = 1
    char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == char:
            count += 1
        else:
            encoded.append(str(count) + char)
            char = s[i]
            count = 1
    
    encoded.append(str(count) + char)
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_strings = ["", "A", "AAABBBCCC", "aabcccccaaa", "XYZ"]
    for s in sample_strings:
        result = run_length_encode(s)
        print(result)