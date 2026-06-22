import math

def compress_floats(data):
    if not data:
        return []
    
    compressed = []
    current_value = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if math.isnan(data[i]):
            if math.isnan(current_value):
                count += 1
            else:
                compressed.append((current_value, count))
                current_value = data[i]
                count = 1
        elif math.isnan(current_value):
            compressed.append((current_value, count))
            current_value = data[i]
            count = 1
        elif abs(data[i] - current_value) < 1e-9:
            count += 1
        else:
            compressed.append((current_value, count))
            current_value = data[i]
            count = 1
            
    compressed.append((current_value, count))
    return compressed

def decompress_floats(compressed):
    result = []
    for value, count in compressed:
        result.extend([value] * count)
    return result

if __name__ == '__main__':
    sample_data = [1.0, 1.0, 1.0, 2.5, 2.5, 3.14159, 3.14159, 3.14159, 3.14159, 5.0]
    compressed_result = compress_floats(sample_data)
    print(compressed_result)
    decompressed_result = decompress_floats(compressed_result)
    print(decompressed_result)