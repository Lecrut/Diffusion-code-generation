def decompress_rle(encoded_string):
    decompressed = []
    i = 0
    while i < len(encoded_string):
        if encoded_string[i].isdigit():
            raise ValueError("Invalid RLE string: number found at start of segment")
        char = encoded_string[i]
        i += 1
        num_str = ""
        while i < len(encoded_string) and encoded_string[i].isdigit():
            num_str += encoded_string[i]
            i += 1
        if num_str == "":
            count = 1
        else:
            count = int(num_str)
        decompressed.append(char * count)
    return "".join(decompressed)

if __name__ == '__main__':
    sample1 = "A5B2C1"
    sample2 = "H3e2l3o1"
    sample3 = "a1b1c1"
    print(decompress_rle(sample1))
    print(decompress_rle(sample2))
    print(decompress_rle(sample3))