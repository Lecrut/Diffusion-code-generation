def rle_encode(s: str) -> str:
    if not s:
        return ''
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f'{count}{current_char}')
            current_char = char
            count = 1
    result.append(f'{count}{current_char}')
    return ''.join(result)

def rle_decode(s: str) -> str:
    if not s:
        return ''
    result = []
    i = 0
    length = len(s)
    while i < length:
        num_str = ''
        while i < length and s[i].isdigit():
            num_str += s[i]
            i += 1
        count = int(num_str)
        if i < length:
            char = s[i]
            result.append(char * count)
            i += 1
    return ''.join(result)
if __name__ == '__main__':
    encoded = rle_encode('aaabbc')
    print(encoded)
    decoded = rle_decode(encoded)
    print(decoded)
    print(rle_encode(''))
    print(rle_decode(''))
    print(rle_encode('abcdef'))
    print(rle_decode('1a1b1c1d1e1f'))