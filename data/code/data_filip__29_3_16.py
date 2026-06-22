def encode_string(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(current_char + str(count))
            else:
                result.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        result.append(current_char + str(count))
    else:
        result.append(current_char)
    return "".join(result)

if __name__ == '__main__':
    print(encode_string("aabbc"))
    print(encode_string("hello"))
    print(encode_string("aaaa"))
    print(encode_string("abc"))
    print(encode_string(""))