import itertools
import re

def rle_compress(data: str) -> str:
    if not data:
        return ''
    grouped = itertools.groupby(data)
    result = []
    for char, group in grouped:
        length = len(list(group))
        if length > 1:
            result.append(f'{length}{char}')
        else:
            result.append(char)
    return ''.join(result)

def rle_decompress(data: str) -> str:
    if not data:
        return ''
    pattern = re.compile('(\\d+)(\\D)')

    def replacer(match):
        count = int(match.group(1))
        char = match.group(2)
        return char * count
    decompressed = pattern.sub(replacer, data)
    result_parts = []
    i = 0
    length = len(data)
    while i < length:
        if data[i].isdigit():
            j = i
            while j < length and data[j].isdigit():
                j += 1
            count = int(data[i:j])
            if j < length:
                char = data[j]
                result_parts.append(char * count)
                i = j + 1
            else:
                result_parts.append(data[i:])
                break
        else:
            result_parts.append(data[i])
            i += 1
    return ''.join(result_parts)
if __name__ == '__main__':
    original = 'AAABBBCCD'
    compressed = rle_compress(original)
    decompressed = rle_decompress(compressed)
    print(compressed)
    print(decompressed)
    print(compressed == '3A3B2C1D')
    print(decompressed == original)