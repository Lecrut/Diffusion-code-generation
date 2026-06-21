def int_to_binary_reverse_construction(n):
    if n == 0:
        return '0'
    bits = []
    while n > 0:
        bit = n % 2
        bits.append(str(bit))
        n = n // 2
    bits.reverse()
    return ''.join(bits)

if __name__ == '__main__':
    sample_values = [0, 1, 2, 5, 10, 42, 255]
    for val in sample_values:
        result = int_to_binary_reverse_construction(val)
        print(f"{val}: {result}")