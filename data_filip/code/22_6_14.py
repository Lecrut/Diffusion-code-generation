def rle_compress(s):
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    result.append(f"{current_char}{count}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbbcccaaa"
    compressed = rle_compress(sample_string)
    print(compressed)