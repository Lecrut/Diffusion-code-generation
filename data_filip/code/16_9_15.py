import math

def compress_floats(data, tolerance=1e-9):
    if not data:
        return []
    
    compressed = []
    current_value = data[0]
    run_length = 1
    
    for i in range(1, len(data)):
        if math.isclose(data[i], current_value, abs_tol=tolerance):
            run_length += 1
        else:
            compressed.append((current_value, run_length))
            current_value = data[i]
            run_length = 1
            
    compressed.append((current_value, run_length))
    return compressed

if __name__ == '__main__':
    sample_data = [1.0, 1.0, 1.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0, 4.0]
    result = compress_floats(sample_data)
    print(result)