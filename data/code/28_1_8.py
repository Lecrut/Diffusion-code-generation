def decode_rle(rle_list):
    if not rle_list:
        return ""
    result = []
    for char, count in rle_list:
        result.append(char * count)
    return "".join(result)

if __name__ == "__main__":
    encoded_data = [('a', 5), ('b', 2), ('c', 10)]
    decoded_string = decode_rle(encoded_data)
    print(decoded_string)