def decompress_rle(compressed: str) -> str:
    result = []
    i = 0
    n = len(compressed)
    while i < n:
        char = compressed[i]
        i += 1
        if i >= n or not compressed[i].isdigit():
            result.append(char)
        else:
            num_str = []
            while i < n and compressed[i].isdigit():
                num_str.append(compressed[i])
                i += 1
            count = int(''.join(num_str))
            if count < 0:
                raise ValueError("Count cannot be negative")
            result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    compressed_string = "a3b2c1d4"
    original = decompress_rle(compressed_string)
    print(original)