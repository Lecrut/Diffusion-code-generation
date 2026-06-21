def rle_decode(compressed: str) -> str:
    if not compressed:
        return ''
    result = []
    i = 0
    n = len(compressed)
    while i < n:
        char = compressed[i]
        i += 1
        count_str = []
        while i < n and compressed[i].isdigit():
            count_str.append(compressed[i])
            i += 1
        if count_str:
            count = int(''.join(count_str))
        else:
            count = 1
        result.append(char * count)
    return ''.join(result)
if __name__ == '__main__':
    compressed_input = 'a3b1c2d3'
    decoded_output = rle_decode(compressed_input)
    print(decoded_output)