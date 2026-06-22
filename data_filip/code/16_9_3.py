import math

def run_length_encode_floats(data, tolerance=1e-9):
    if not data:
        return []
    
    encoded = []
    current_value = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if math.isclose(data[i], current_value, abs_tol=tolerance):
            count += 1
        else:
            encoded.append((current_value, count))
            current_value = data[i]
            count = 1
    
    encoded.append((current_value, count))
    return encoded

if __name__ == '__main__':
    sample_data = [1.0, 1.0, 1.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0, 1.0000000001]
    result = run_length_encode_floats(sample_data)
    print(result)