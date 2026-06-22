def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    chars = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                chars.append(str(count))
            chars.append(current_char)
            current_char = s[i]
            count = 1
    
    if count > 1:
        chars.append(str(count))
    chars.append(current_char)
    
    return "".join(chars)

if __name__ == '__main__':
    print(run_length_encode("aabcccccaaa"))
    print(run_length_encode("abc"))
    print(run_length_encode(""))
    print(run_length_encode("a"))
    print(run_length_encode("aaabbbccc"))