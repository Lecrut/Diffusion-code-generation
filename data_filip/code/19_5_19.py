def rle_encode(data, max_run=15):
    if not data:
        return []
    if len(data) == 1:
        return [1, data[0]]
    result = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char and count < max_run:
            count += 1
        else:
            result.append(count)
            result.append(current_char)
            current_char = data[i]
            count = 1
    while count > 0:
        if count > max_run:
            result.append(max_run)
            result.append(current_char)
            count -= max_run
        else:
            result.append(count)
            result.append(current_char)
            count = 0
    return result

if __name__ == '__main__':
    sample_input = "AAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBB"
    encoded = rle_encode(sample_input, 15)
    print(encoded)