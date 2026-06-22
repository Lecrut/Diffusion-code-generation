def decompress_rle(encoded_str):
    if not encoded_str:
        return ""
    result = [char * int(count) for char, count in [(encoded_str[i], encoded_str[i+1]) for i in range(0, len(encoded_str), 2)]]
    return ''.join(result)

if __name__ == '__main__':
    print(decompress_rle("a3b2c1d4"))