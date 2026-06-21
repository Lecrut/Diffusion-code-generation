def rle_encode(s):
    if not s:
        return ""
    encoded = []
    i = 0
    n = len(s)
    while i < n:
        current_char = s[i]
        count = 1
        i += 1
        while i < n and s[i] == current_char:
            count += 1
            i += 1
        encoded.append(str(count) + current_char)
    return "".join(encoded)

if __name__ == '__main__':
    test_string = "aaabbcdddd"
    result = rle_encode(test_string)
    print(result)
    test_string2 = "a"
    result2 = rle_encode(test_string2)
    print(result2)
    test_string3 = ""
    result3 = rle_encode(test_string3)
    print(result3)