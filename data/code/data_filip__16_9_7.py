import math

def compress_rle_float(data, tolerance=1e-9):
    if not data:
        return []
    
    result = []
    current_val = data[0]
    current_count = 1
    
    for i in range(1, len(data)):
        val = data[i]
        if math.isclose(val, current_val, rel_tol=tolerance, abs_tol=tolerance):
            current_count += 1
        else:
            result.append((current_val, current_count))
            current_val = val
            current_count = 1
            
    result.append((current_val, current_count))
    return result

if __name__ == '__main__':
    sample_data = [1.0, 1.0, 1.0, 2.0, 2.0, 3.5, 3.5, 3.5, 3.5, 4.0]
    compressed = compress_rle_float(sample_data)
    print(compressed)