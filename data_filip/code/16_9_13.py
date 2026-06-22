import math

def compress_rle(data):
    if not data:
        return []
    result = []
    current_val = data[0]
    count = 1
    n = len(data)
    for i in range(1, n):
        val = data[i]
        if math.isclose(val, current_val, rel_tol=0, abs_tol=1e-9):
            count += 1
        else:
            result.append((current_val, count))
            current_val = val
            count = 1
    result.append((current_val, count))
    return result

if __name__ == '__main__':
    sample_data = [1.5, 1.5, 1.5, 2.0, 3.0, 3.0, 3.0, 3.0, 1.5]
    compressed = compress_rle(sample_data)
    print(compressed)