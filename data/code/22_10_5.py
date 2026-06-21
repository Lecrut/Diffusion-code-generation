def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    compressed = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(current_char)
            if count > 1:
                compressed.append(str(count))
            current_char = s[i]
            count = 1
    
    compressed.append(current_char)
    if count > 1:
        compressed.append(str(count))
    
    return "".join(compressed)

if __name__ == '__main__':
    print(run_length_encode(""))
    print(run_length_encode("A"))
    print(run_length_encode("AA"))
    print(run_length_encode("AABBBCCC"))
    print(run_length_encode("ABC"))
    print(run_length_encode("AAAAAAAAAAABBBBBBBBBBBBCCCCCCCCCCCDDDDDDDDDDDD"))
    print(run_length_encode("aabbccddeeff"))
    print(run_length_encode("xyz"))