def decompress_rle(data: str) -> str:
    result = []
    i = 0
    n = len(data)
    while i < n:
        count = 0
        while i < n and data[i].isdigit():
            count = count * 10 + int(data[i])
            i += 1
        if i < n:
            char = data[i]
            result.append(char * count)
            i += 1
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "10A3B2C"
    output = decompress_rle(sample_input)
    print(output)