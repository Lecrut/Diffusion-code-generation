def decode_rle(encoded_list: list[tuple[str, int]]) -> str:
    result = []
    for char, count in encoded_list:
        result.append(char * count)
    return ''.join(result)
if __name__ == '__main__':
    encoded_data = [('a', 3), ('b', 2), ('c', 5)]
    decoded_string = decode_rle(encoded_data)
    print(decoded_string)