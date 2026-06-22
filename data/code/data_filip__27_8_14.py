def rle_encode(data):
    if not data:
        return ''

    parts = []
    count = 1
    current_char = data[0]

    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            parts.append(str(count))
            parts.append(current_char)
            current_char = data[i]
            count = 1

    parts.append(str(count))
    parts.append(current_char)

    return ''.join(parts)

if __name__ == '__main__':
    sample_string = 'WWWWWWWWWWWWWBWWWWWWWWWWWWWWWBWWWWWWWWWWWWWWCCCCCCCCCC'
    result = rle_encode(sample_string)
    print(result)