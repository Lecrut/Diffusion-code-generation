def run_length_encode(s: str) -> str:
    if not s:
        return s
    
    result = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        result.append(str(count))
    result.append(current_char)
    
    compressed = ''.join(result)
    return compressed if len(compressed) < len(s) else s

if __name__ == '__main__':
    print(run_length_encode(""))
    print(run_length_encode("a"))
    print(run_length_encode("aa"))
    print(run_length_encode("aaa"))
    print(run_length_encode("aabbbcc"))
    print(run_length_encode("abc"))
    print(run_length_encode("aabbbcccc"))
    print(run_length_encode("aaabbbccc"))
    print(run_length_encode("aabb"))
    print(run_length_encode("abcabc"))