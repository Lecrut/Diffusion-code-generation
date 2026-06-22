def rle_decode(compressed: str) -> str:
    result = []
    num_buffer = []
    for char in compressed:
        if char.isdigit():
            num_buffer.append(char)
        else:
            if num_buffer:
                count = int(''.join(num_buffer))
                num_buffer = []
                result.append(char * count)
            else:
                result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    print(rle_decode("a3b2c1"))
    print(rle_decode("z10a1"))
    print(rle_decode("abc"))
    print(rle_decode(""))