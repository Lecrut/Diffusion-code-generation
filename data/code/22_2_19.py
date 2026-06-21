def decompress_rle(encoded: str) -> str:
    result = []
    count = 0
    for char in encoded:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            if count > 0:
                result.append(char * count)
            else:
                result.append(char)
            count = 0
    return "".join(result)

if __name__ == '__main__':
    sample_input = "a10b3c2d1"
    output = decompress_rle(sample_input)
    print(output)