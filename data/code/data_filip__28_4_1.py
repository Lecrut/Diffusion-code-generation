def encode_rle(data):
    if not data:
        return []
    result = []
    current_value = data[0]
    count = 1
    for value in data[1:]:
        if value == current_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = value
            count = 1
    result.append((current_value, count))
    return result

if __name__ == '__main__':
    sample_list = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]
    encoded_list = encode_rle(sample_list)
    print(encoded_list)