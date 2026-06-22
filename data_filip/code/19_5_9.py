def rle_encode_with_limit(data, max_run):
    if not data:
        return []
    result = []
    i = 0
    while i < len(data):
        current_char = data[i]
        count = 1
        while i + count < len(data) and data[i + count] == current_char and count < max_run:
            count += 1
        result.append((current_char, count))
        i += count
    return result

if __name__ == '__main__':
    sample_data = 'AAAABBBCCDAA'
    max_run_length = 3
    encoded_result = rle_encode_with_limit(sample_data, max_run_length)
    print(encoded_result)