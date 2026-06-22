def decompress_rle(s):
    if not s:
        return []
    result = []
    chars = list(s)
    i = 0
    n = len(chars)
    while i < n:
        if i + 1 < n and chars[i+1].isdigit():
            count = int(chars[i+1])
            result.extend([chars[i]] * count)
            i += 2
        else:
            result.append(chars[i])
            i += 1
    return result

if __name__ == '__main__':
    sample_input = "a3b2c5"
    print(decompress_rle(sample_input))