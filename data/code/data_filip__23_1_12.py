def run_length_encode(data):
    if not data:
        return []
    encoded = []
    count = 1
    current_char = data[0]
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = data[i]
            count = 1
    encoded.append((current_char, count))
    return encoded

def run_length_decode(encoded_data):
    decoded = []
    for char, count in encoded_data:
        decoded.append(char * count)
    return ''.join(decoded)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded_result = run_length_encode(sample_input)
    print(f"Encoded: {encoded_result}")
    decoded_result = run_length_decode(encoded_result)
    print(f"Decoded: {decoded_result}")