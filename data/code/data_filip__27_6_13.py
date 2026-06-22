def rle_encode_byte_optimized(s):
    if not s:
        return []
    result = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = s[i]
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_string = "AAABBBCCDAA"
    result = rle_encode_byte_optimized(sample_string)
    print(result)