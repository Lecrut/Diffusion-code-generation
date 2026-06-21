def run_length_encode(s):
    if not s:
        return ""
    
    compressed = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(current_char)
            compressed.append(str(count))
            current_char = char
            count = 1
    
    compressed.append(current_char)
    compressed.append(str(count))
    
    return ''.join(compressed)

if __name__ == '__main__':
    print(run_length_encode(""))
    print(run_length_encode("a"))
    print(run_length_encode("aaa"))
    print(run_length_encode("aabbcccc"))
    print(run_length_encode("abc"))
    print(run_length_encode("aaabba"))