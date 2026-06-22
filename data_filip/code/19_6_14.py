def rle_encode_case_insensitive(data):
    if not data:
        return ""
    data = data.lower()
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    return "".join(encoded)

if __name__ == '__main__':
    sample_input = "AAABBBccDaAa"
    result = rle_encode_case_insensitive(sample_input)
    print(result)