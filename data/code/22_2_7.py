def decompress_rle(encoded_str):
    result = []
    i = 0
    while i < len(encoded_str):
        if encoded_str[i].isdigit():
            j = i
            while j < len(encoded_str) and encoded_str[j].isdigit():
                j += 1
            count = int(encoded_str[i:j])
            char = encoded_str[j]
            result.extend([char] * count)
            i = j + 1
        else:
            result.append(encoded_str[i])
            i += 1
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "3A2B5C1D"
    output = decompress_rle(sample_input)
    print(output)