def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    compressed = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                compressed.append(f"{current_char}{count}")
            else:
                compressed.append(current_char)
            current_char = s[i]
            count = 1
    
    if count > 1:
        compressed.append(f"{current_char}{count}")
    else:
        compressed.append(current_char)
    
    return "".join(compressed)

if __name__ == '__main__':
    print(run_length_encode("aabcccccaaa"))
    print(run_length_encode("abcdef"))
    print(run_length_encode("aaabbbccc"))
    print(run_length_encode("a"))
    print(run_length_encode(""))