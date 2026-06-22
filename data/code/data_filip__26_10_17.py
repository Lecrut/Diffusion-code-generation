def rle_encode(s):
    if not s:
        return ""
    encoded = []
    i = 0
    n = len(s)
    while i < n:
        count = 1
        current_char = s[i]
        while i + 1 < n and s[i + 1] == current_char:
            count += 1
            i += 1
        encoded.append(f"{count}{current_char}")
        i += 1
    return "".join(encoded)

if __name__ == '__main__':
    test_string = "aaabbbcccaad"
    result = rle_encode(test_string)
    print(result)