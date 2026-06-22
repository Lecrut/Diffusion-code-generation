def run_length_encode(data):
    if not data:
        return []
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1
    encoded.append((current_char, count))
    return encoded

def run_length_decode(encoded):
    decoded = []
    for char, count in encoded:
        decoded.append(char * count)
    return ''.join(decoded)

if __name__ == '__main__':
    sample_data = 'AAAABBBCCDAA'
    encoded_data = run_length_encode(sample_data)
    print(encoded_data)
    decoded_data = run_length_decode(encoded_data)
    print(decoded_data)