def large_int_to_binary_string(n):
    if n == 0:
        return "0"
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n == 1:
        return "1"
    
    result = []
    while n > 0:
        bit = n & 1
        result.append(str(bit))
        n >>= 1
    
    result.reverse()
    return "".join(result)

if __name__ == '__main__':
    sample_values = [0, 1, 10, 255, 1024, 65535, 1000000]
    
    for val in sample_values:
        binary_str = large_int_to_binary_string(val)
        print(binary_str)