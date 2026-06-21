import math

def compress_floats(data, tolerance=1e-6):
    if not data:
        return []
    
    encoded = []
    current_value = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if math.isclose(data[i], current_value, rel_tol=tolerance, abs_tol=tolerance):
            count += 1
        else:
            encoded.append((current_value, count))
            current_value = data[i]
            count = 1
    
    encoded.append((current_value, count))
    return encoded

def decompress_floats(encoded):
    decompressed = []
    for value, count in encoded:
        decompressed.extend([value] * count)
    return decompressed

if __name__ == '__main__':
    sample_data = [1.0, 1.0, 1.0, 2.0, 2.0, 3.0, 1.0, 1.0, 1.0, 1.0]
    compressed = compress_floats(sample_data)
    print(compressed)
    decompressed = decompress_floats(compressed)
    print(decompressed)