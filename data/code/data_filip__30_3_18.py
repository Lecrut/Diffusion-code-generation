def int_to_binary(n):
    if n < 0:
        raise ValueError("Only non-negative integers are supported")
    if n == 0:
        return "0"
    
    bits = []
    while n > 0:
        bit = n & 1
        bits.append(str(bit))
        n >>= 1
    
    return "".join(reversed(bits))

if __name__ == '__main__':
    sample_values = [0, 1, 2, 5, 10, 100, 255, 1024, 123456789012345678901234567890]
    
    for value in sample_values:
        result = int_to_binary(value)
        print(f"{value}: {result}")