def rle_encode(s):
    if not s:
        return ""
    
    encoded_parts = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                encoded_parts.append(str(count))
            encoded_parts.append(current_char)
            current_char = s[i]
            count = 1
    
    if count > 1:
        encoded_parts.append(str(count))
    encoded_parts.append(current_char)
    
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_inputs = [
        "",
        "a",
        "abc",
        "aaa",
        "aabbccc",
        "aaabbbcccaaa",
        "hello",
        "mississippi",
        "11122233",
        "abcdefg"
    ]
    
    for sample in sample_inputs:
        print(rle_encode(sample))