def rle_encode(s):
    if not s:
        return ""
    result = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = s[i]
            count = 1
    result.append(str(count))
    result.append(current_char)
    return "".join(result)

if __name__ == '__main__':
    sample_string = "AAABBBCCCD"
    compressed = rle_encode(sample_string)
    print(compressed)