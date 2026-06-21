def rle_encode(s):
    if not s:
        return {}
    result = {}
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result[current_char] = count
            current_char = char
            count = 1
    result[current_char] = count
    return result

if __name__ == '__main__':
    text = "aaabbc"
    encoded = rle_encode(text)
    print(encoded)