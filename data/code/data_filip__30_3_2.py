def large_int_to_binary_string(n):
    if n == 0:
        return '0'
    negative = False
    if n < 0:
        negative = True
        n = -n
    bits = []
    while n > 0:
        bits.append('1' if n & 1 else '0')
        n >>= 1
    bits.reverse()
    result = ''.join(bits)
    if negative:
        result = '-' + result
    return result

if __name__ == '__main__':
    samples = [0, 1, 255, 1024, 16**128, -(1024)]
    for val in samples:
        print(f"{val} -> {large_int_to_binary_string(val)}")