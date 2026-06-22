def decompress_rle(compressed: str) -> str:
    result = []
    i = 0
    n = len(compressed)
    while i < n:
        char = compressed[i]
        if not char.isdigit():
            result.append(char)
            i += 1
        else:
            j = i
            while j < n and compressed[j].isdigit():
                j += 1
            count_str = compressed[i:j]
            count = int(count_str)
            prev_char = result[-1]
            result.append(prev_char * count)
            i = j
    return ''.join(result)

if __name__ == '__main__':
    sample_compressed = "3A3B"
    print(decompress_rle(sample_compressed))