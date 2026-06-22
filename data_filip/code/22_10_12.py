def run_length_encode(s):
    if not s:
        return ""
    
    compressed = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(current_char)
            compressed.append(str(count))
            current_char = s[i]
            count = 1
    
    compressed.append(current_char)
    compressed.append(str(count))
    
    return "".join(compressed)

if __name__ == '__main__':
    sample1 = "AAAABBBCCDAA"
    print(run_length_encode(sample1))
    
    sample2 = "ABCDE"
    print(run_length_encode(sample2))
    
    sample3 = ""
    print(run_length_encode(sample3))
    
    sample4 = "A"
    print(run_length_encode(sample4))
    
    sample5 = "AABBCC"
    print(run_length_encode(sample5))