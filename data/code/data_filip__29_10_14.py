def encode_consecutive_chars(s):
    if not s:
        return ''
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = char
            count = 1
    result.append(current_char + str(count))
    return ''.join(result)

if __name__ == '__main__':
    print(encode_consecutive_chars('aabbbc'))
    print(encode_consecutive_chars('a'))
    print(encode_consecutive_chars(''))
    print(encode_consecutive_chars('aaaa'))