import itertools
import math

def run_length_encode(data):
    if not data:
        return []
    
    encoded = []
    current_value = data[0]
    count = 1
    
    for i in range(1, len(data)):
        value = data[i]
        if value == current_value:
            count += 1
        else:
            encoded.append((current_value, count))
            current_value = value
            count = 1
            
    encoded.append((current_value, count))
    return encoded

def run_length_decode(encoded_data):
    decoded = []
    for value, count in encoded_data:
        decoded.extend([value] * count)
    return decoded

if __name__ == '__main__':
    sample_data = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4]
    encoded_result = run_length_encode(sample_data)
    decoded_result = run_length_decode(encoded_result)
    print(f"Original: {sample_data}")
    print(f"Encoded: {encoded_result}")
    print(f"Decoded: {decoded_result}")
    print(f"Match: {sample_data == decoded_result}")