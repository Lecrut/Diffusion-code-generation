def rle_encode(data):
    if not data:
        return ""
    encoded = []
    count = 1
    current_char = data[0]
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append(str(count))
            encoded.append(current_char)
            current_char = data[i]
            count = 1
    encoded.append(str(count))
    encoded.append(current_char)
    return "".join(encoded)

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAA"
    print(rle_encode(sample_string))