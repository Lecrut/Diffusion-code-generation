def rle_with_max_run(data, max_run):
    if not data:
        return []
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char and count < max_run:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_data = 'AAAABBBCCDAA'
    sample_max_run = 3
    result = rle_with_max_run(sample_data, sample_max_run)
    print(result)