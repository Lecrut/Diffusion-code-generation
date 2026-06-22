import sys

def run_length_encode(data):
    if not data:
        return bytearray()
    
    result = bytearray()
    current_byte = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_byte and count < 255:
            count += 1
        else:
            result.append(count)
            result.append(current_byte)
            current_byte = data[i]
            count = 1
            
    result.append(count)
    result.append(current_byte)
    return result

if __name__ == '__main__':
    sample_input = bytearray([72, 72, 72, 101, 101, 108, 108, 111, 32, 32, 32])
    encoded_result = run_length_encode(sample_input)
    print(list(encoded_result))