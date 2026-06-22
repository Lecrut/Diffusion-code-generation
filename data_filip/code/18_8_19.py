def rle_encode(data):
    if not data:
        return []
    encoded = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append(current_char)
            encoded.append(count)
            current_char = data[i]
            count = 1
    encoded.append(current_char)
    encoded.append(count)
    return encoded

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAA"
    result = rle_encode(sample_string)
    print(result)