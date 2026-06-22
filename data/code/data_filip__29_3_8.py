def encode_string(s):
    if not s:
        return ""

    encoded = []
    current_char = s[0]
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(current_char + str(count))
            current_char = char
            count = 1

    encoded.append(current_char + str(count))
    return "".join(encoded)

if __name__ == '__main__':
    print(encode_string("aabcccccaaa"))
    print(encode_string("abcd"))
    print(encode_string("aaaa"))
    print(encode_string(""))
    print(encode_string("a"))
    print(encode_string("aabba"))