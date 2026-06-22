def enhance_rle_encode(data: str) -> str:
    if not data:
        return ''
    result = []
    count = 1
    i = 1
    n = len(data)
    while i < n:
        char = data[i]
        prev_char = data[i - 1]
        if char == prev_char:
            count += 1
        else:
            result.append(_format_run(prev_char, count))
            count = 1
        i += 1
    result.append(_format_run(data[-1], count))
    return ''.join(result)

def _format_run(char: str, count: int) -> str:
    if count > 1:
        if char.isdigit():
            return f'{count}\\{char}'
        else:
            return f'{count}{char}'
    elif char.isdigit():
        return f'{count}\\{char}'
    else:
        return f'{count}{char}'

def enhance_rle_decode(data: str) -> str:
    if not data:
        return ''
    result = []
    i = 0
    n = len(data)
    while i < n:
        count_str = ''
        while i < n and data[i].isdigit():
            count_str += data[i]
            i += 1
        if not count_str:
            raise ValueError('Invalid RLE data: missing count')
        count = int(count_str)
        if i >= n:
            raise ValueError('Invalid RLE data: missing character')
        char = data[i]
        i += 1
        if char == '\\':
            if i >= n:
                raise ValueError('Invalid RLE data: incomplete escape')
            literal_char = data[i]
            i += 1
            result.append(literal_char * count)
        else:
            result.append(char * count)
    return ''.join(result)
if __name__ == '__main__':
    encoded = enhance_rle_encode('1222333')
    print(encoded)
    decoded = enhance_rle_decode(encoded)
    print(decoded)
    encoded2 = enhance_rle_encode('aaa')
    print(encoded2)
    decoded2 = enhance_rle_decode(encoded2)
    print(decoded2)
    encoded3 = enhance_rle_encode('abc')
    print(encoded3)
    decoded3 = enhance_rle_decode(encoded3)
    print(decoded3)
    encoded4 = enhance_rle_encode('11122')
    print(encoded4)
    decoded4 = enhance_rle_decode(encoded4)
    print(decoded4)
    encoded5 = enhance_rle_encode('1')
    print(encoded5)
    decoded5 = enhance_rle_decode(encoded5)
    print(decoded5)
    encoded6 = enhance_rle_encode('121')
    print(encoded6)
    decoded6 = enhance_rle_decode(encoded6)
    print(decoded6)