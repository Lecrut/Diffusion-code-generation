def decompress_rle(compressed: str) -> str:
    if not compressed:
        return ''
    result = []
    i = 0
    n = len(compressed)
    while i < n:
        char = compressed[i]
        i += 1
        if char.isdigit():
            num_str = char
            while i < n and compressed[i].isdigit():
                num_str += compressed[i]
                i += 1
            count = int(num_str)
            if i >= n:
                raise ValueError('Compressed string ends with digits but no following character')
            repeat_char = compressed[i]
            i += 1
            result.append(repeat_char * count)
        else:
            result.append(char)
    return ''.join(result)
if __name__ == '__main__':
    compressed_string = '3a2b4c1d'
    original = decompress_rle(compressed_string)
    print(original)
    compressed_string2 = '2w3x'
    original2 = decompress_rle(compressed_string2)
    print(original2)
    compressed_string3 = ''
    original3 = decompress_rle(compressed_string3)
    print(original3)
    compressed_string4 = 'a'
    original4 = decompress_rle(compressed_string4)
    print(original4)
    compressed_string5 = '10z'
    original5 = decompress_rle(compressed_string5)
    print(original5)