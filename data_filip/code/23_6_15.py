import struct

def run_length_encode(data):
    if not data:
        return bytearray()
    
    result = bytearray()
    current_byte = data[0]
    count = 1
    
    for i in range(1, len(data)):
        byte = data[i]
        if byte == current_byte and count < 255:
            count += 1
        else:
            result.append(current_byte)
            result.append(count)
            current_byte = byte
            count = 1
            
    result.append(current_byte)
    result.append(count)
    
    return result

def run_length_decode(data):
    if not data:
        return bytearray()
    
    if len(data) % 2 != 0:
        raise ValueError("Invalid RLE data: odd number of bytes")
    
    result = bytearray()
    
    for i in range(0, len(data), 2):
        byte = data[i]
        count = data[i + 1]
        result.extend([byte] * count)
        
    return result

if __name__ == '__main__':
    sample_input = b'AAAAABBBCCCCCCDDDDD'
    encoded = run_length_encode(sample_input)
    decoded = run_length_decode(encoded)
    
    print("Original:", sample_input)
    print("Encoded:", list(encoded))
    print("Decoded:", decoded)
    print("Match:", sample_input == decoded)
    
    large_input = bytes([i % 256] * 1000 for i in range(10))
    large_encoded = run_length_encode(large_input)
    large_decoded = run_length_decode(large_encoded)
    print("Large input length:", len(large_input))
    print("Large encoded length:", len(large_encoded))
    print("Large match:", large_input == large_decoded)