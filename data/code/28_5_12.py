def encode_rle(s):
    if not s:
        return ''
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = char
            count = 1
    result.append(str(count) + current_char)
    return ''.join(result)

def decode_rle(s):
    if not s:
        return ''
    result = []
    i = 0
    while i < len(s):
        count_str = ''
        while i < len(s) and s[i].isdigit():
            count_str += s[i]
            i += 1
        if i < len(s):
            char = s[i]
            count = int(count_str)
            result.append(char * count)
            i += 1
    return ''.join(result)

if __name__ == '__main__':
    original = "AAABBBCCDAA"
    encoded = encode_rle(original)
    decoded = decode_rle(encoded)
    print(decoded == original)