def decode_run_length(encoded_list):
    result = []
    for char, count in encoded_list:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    sample_data = [('a', 5), ('b', 2), ('c', 3), ('d', 1)]
    decoded_string = decode_run_length(sample_data)
    print(decoded_string)