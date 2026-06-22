def rle_encode(data):
    if not data:
        return ''
    result = []
    prev_char = data[0]
    count = 1
    for char, next_char in zip(data, data[1:]):
        if char == next_char:
            count += 1
        else:
            result.append(str(count) + char)
            count = 1
    result.append(str(count) + prev_char)
    return ''.join(result)

if __name__ == '__main__':
    sample_input = 'AAAAABBBB'
    encoded_result = rle_encode(sample_input)
    print(encoded_result)