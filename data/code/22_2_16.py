def decompress_rle(encoded_string):
    if not encoded_string:
        return ""
    result = []
    i = 0
    length = len(encoded_string)
    while i < length:
        if not encoded_string[i].isdigit():
            result.append(encoded_string[i])
            i += 1
        else:
            j = i
            while j < length and encoded_string[j].isdigit():
                j += 1
            count = int(encoded_string[i:j])
            if j < length:
                result.append(encoded_string[j] * count)
                i = j + 1
            else:
                i = j
    return "".join(result)

if __name__ == '__main__':
    sample_input = "3a2b4c1d"
    output = decompress_rle(sample_input)
    print(output)