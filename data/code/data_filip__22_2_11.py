def decompress_rle(encoded: str) -> str:
    pairs = [(int(encoded[i]), encoded[i + 1]) for i in range(0, len(encoded), 2)]
    return ''.join(char * count for count, char in pairs)

if __name__ == '__main__':
    test1 = "2a3b1c"
    print(decompress_rle(test1))
    test2 = "1H1e2l2o"
    print(decompress_rle(test2))
    test3 = "10x"
    print(decompress_rle(test3))
    test4 = ""
    print(decompress_rle(test4))
    test5 = "1A2B3C"
    print(decompress_rle(test5))