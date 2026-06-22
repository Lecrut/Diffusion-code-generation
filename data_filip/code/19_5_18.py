def rle_encode(data, max_run=255):
    if not data:
        return []
    
    encoded = []
    current_char = data[0]
    count = 1
    
    for char in data[1:]:
        if char == current_char:
            count += 1
            if count == max_run:
                encoded.append((current_char, count))
                current_char = char
                count = 0
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1
    
    if count > 0:
        encoded.append((current_char, count))
    
    return encoded

def rle_decode(encoded):
    decoded = []
    for char, count in encoded:
        decoded.append(char * count)
    return "".join(decoded)

if __name__ == '__main__':
    sample_data = "A" * 300 + "B" * 100 + "C" * 50 + "D"
    encoded_result = rle_encode(sample_data, max_run=100)
    decoded_result = rle_decode(encoded_result)
    print(f"Original length: {len(sample_data)}")
    print(f"Encoded segments: {len(encoded_result)}")
    print(f"Decoded matches original: {decoded_result == sample_data}")
    print(f"First 3 encoded pairs: {encoded_result[:3]}")
    print(f"Last encoded pair: {encoded_result[-1]}")