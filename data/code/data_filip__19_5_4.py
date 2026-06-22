def rle_encode(data, max_run=255):
    if not data:
        return []
    result = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char and count < max_run:
            count += 1
        else:
            while count > 0:
                split_count = min(count, max_run)
                result.append((current_char, split_count))
                count -= split_count
            current_char = data[i]
            count = 1
    while count > 0:
        split_count = min(count, max_run)
        result.append((current_char, split_count))
        count -= split_count
    return result

if __name__ == '__main__':
    sample_data = "AAAAAAABBBBCCCCDDDDD"
    encoded_result = rle_encode(sample_data, 4)
    print(encoded_result)