def decompress_rle(encoded_str):
    result = []
    i = 0
    n = len(encoded_str)
    while i < n:
        char = encoded_str[i]
        i += 1
        num_str = []
        while i < n and encoded_str[i].isdigit():
            num_str.append(encoded_str[i])
            i += 1
        count = int(''.join(num_str)) if num_str else 1
        result.extend([char] * count)
    return ''.join(result)

if __name__ == '__main__':
    sample_encoded = "a3b2c5"
    output = decompress_rle(sample_encoded)
    print(output)