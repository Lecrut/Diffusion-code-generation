def decompress_rle(s):
    if not s:
        return ""
    result = []
    i = 0
    n = len(s)
    while i < n:
        if not s[i].isdigit():
            raise ValueError("Invalid RLE format: expected digit")
        j = i
        while j < n and s[j].isdigit():
            j += 1
        count = int(s[i:j])
        if j >= n:
            raise ValueError("Invalid RLE format: missing character")
        char = s[j]
        result.append(char * count)
        i = j + 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = "4a2b3c"
    print(decompress_rle(sample_input))
    sample_input_2 = "10z1w2x"
    print(decompress_rle(sample_input_2))