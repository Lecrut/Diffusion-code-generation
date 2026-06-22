def decompress_rle(encoded: str) -> str:
    result = []
    current_num = []
    for char in encoded:
        if char.isdigit():
            current_num.append(char)
        else:
            if current_num:
                count = int(''.join(current_num))
                result.append(char * count)
                current_num = []
            else:
                result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    encoded_string = "2a3b4c"
    decompressed = decompress_rle(encoded_string)
    print(decompressed)