def decode_run_length(rle_data):
    result = []
    for char, count in rle_data:
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    encoded_data = [("a", 5), ("b", 2), ("c", 1)]
    decoded_string = decode_run_length(encoded_data)
    print(decoded_string)