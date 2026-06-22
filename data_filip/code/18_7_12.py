def run_length_encode(data):
    if not data:
        return []
    result = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = data[i]
            count = 1
    result.append((current_char, count))
    return result

def decode_rle(encoded_data):
    result = []
    for char, count in encoded_data:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded = run_length_encode(sample_string)
    print(encoded)
    decoded = decode_rle(encoded)
    print(decoded)
    print(sample_string == decoded)