import sys

def compress_rle(data):
    if not data:
        return []
    
    result = []
    current_count = 1
    current_val = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current_val:
            current_count += 1
        else:
            result.append((current_val, current_count))
            current_val = data[i]
            current_count = 1
    result.append((current_val, current_count))
    
    return result

def decompress_rle(rle_data):
    decompressed = []
    for value, count in rle_data:
        decompressed.extend([value] * count)
    return decompressed

if __name__ == '__main__':
    input_list = [1, 1, 1, 2, 3, 3, 2, 2, 2, 1]
    compressed = compress_rle(input_list)
    print(compressed)
    
    decompressed = decompress_rle(compressed)
    print(decompressed)