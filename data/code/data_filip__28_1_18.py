def decode_rle(rle_data):
    if not rle_data:
        return ''
    result_parts = []
    i = 0
    while i < len(rle_data):
        char = rle_data[i]
        count_str = ''
        i += 1
        while i < len(rle_data) and rle_data[i].isdigit():
            count_str += rle_data[i]
            i += 1
        count = int(count_str) if count_str else 1
        result_parts.append(char * count)
    return ''.join(result_parts)

if __name__ == '__main__':
    sample_rle = ['a', '3', 'b', '2', 'c', '1']
    decoded_string = decode_rle(sample_rle)
    print(decoded_string)