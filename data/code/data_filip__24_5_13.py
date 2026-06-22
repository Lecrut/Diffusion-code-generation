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
            encoded.append((count, current_char))
            current_char = char
            count = 1
    encoded.append((count, current_char))
    return encoded

def run_length_decode(encoded_data):
    decoded = []
    for count, char in encoded_data:
        decoded.append(char * count)
    return ''.join(decoded)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)
    decoded_result = run_length_decode(encoded_result)
    print(decoded_result)