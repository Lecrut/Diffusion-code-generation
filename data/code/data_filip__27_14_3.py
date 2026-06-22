def rle_encode(s):
    if not s:
        return ""
    result = []
    count = 1
    current = s[0]
    for char in s[1:]:
        if char == current:
            count += 1
        else:
            result.append(f"{count}{current}")
            current = char
            count = 1
    result.append(f"{count}{current}")
    return "".join(result)

if __name__ == '__main__':
    test_string = "AAABBBCCCCD"
    encoded = rle_encode(test_string)
    print(encoded)