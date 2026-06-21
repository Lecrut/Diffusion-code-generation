def decode_rle(encoded_list):
    return "".join(char * count for char, count in encoded_list)

if __name__ == '__main__':
    sample_rle = [("a", 5), ("b", 2), ("c", 1)]
    result = decode_rle(sample_rle)
    print(result)