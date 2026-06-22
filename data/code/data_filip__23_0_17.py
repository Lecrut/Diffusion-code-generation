def run_length_encode(s):
    if not s:
        return ""
    
    compressed = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(f"{count}{current_char}")
            current_char = s[i]
            count = 1
    
    compressed.append(f"{count}{current_char}")
    
    result = "".join(compressed)
    
    if len(result) >= len(s):
        return s
    
    return result

if __name__ == '__main__':
    print(run_length_encode(""))
    print(run_length_encode("a"))
    print(run_length_encode("aabcccccaaa"))
    print(run_length_encode("abc"))
    print(run_length_encode("aaaaa"))
    print(run_length_encode("aabbcc"))
    print(run_length_encode("abcdef"))
    print(run_length_encode("zzzzzzzzzz"))