def run_length_encode(data: bytearray) -> bytearray:
    if not data:
        return bytearray()
    
    result = bytearray()
    count = 1
    current_byte = data[0]
    
    for i in range(1, len(data)):
        byte = data[i]
        if byte == current_byte and count < 255:
            count += 1
        else:
            result.append(count)
            result.append(current_byte)
            current_byte = byte
            count = 1
    
    result.append(count)
    result.append(current_byte)
    
    return result

def run_length_decode(data: bytearray) -> bytearray:
    if not data:
        return bytearray()
    
    if len(data) % 2 != 0:
        raise ValueError("Invalid RLE data: odd length")
    
    result = bytearray()
    for i in range(0, len(data), 2):
        count = data[i]
        value = data[i+1]
        result.extend([value] * count)
    
    return result

if __name__ == '__main__':
    sample_input = bytearray([65, 65, 65, 66, 66, 67, 67, 67, 67, 68])
    encoded = run_length_encode(sample_input)
    print("Encoded:", encoded)
    decoded = run_length_decode(encoded)
    print("Decoded:", decoded)
    print("Original matches decoded:", sample_input == decoded)