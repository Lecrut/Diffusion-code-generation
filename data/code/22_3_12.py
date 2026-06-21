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
            encoded.append((current_char, count))
            current_char = data[i]
            count = 1
    encoded.append((current_char, count))
    return encoded

def rle_decode(encoded_data):
    decoded = []
    for char, count in encoded_data:
        decoded.append(char * count)
    return "".join(decoded)

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded_result = rle_encode(sample_string)
    decoded_result = rle_decode(encoded_result)
    print(encoded_result)
    print(decoded_result)