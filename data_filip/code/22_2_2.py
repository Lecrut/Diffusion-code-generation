def decompress_rle(encoded: str) -> str:
    result = []
    current_num = 0
    for char in encoded:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        else:
            if current_num > 0:
                result.append(char * current_num)
                current_num = 0
            else:
                result.append(char)
    if current_num > 0:
        result.append(encoded[-1] * current_num)
    return "".join(result)

if __name__ == '__main__':
    encoded_str = "a3b4c2d1"
    original_str = decompress_rle(encoded_str)
    print(original_str)