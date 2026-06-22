def large_int_to_binary(n):
    if n == 0:
        return "0"
    if n < 0:
        return "-" + large_int_to_binary(-n)
    bits = []
    while n > 0:
        bits.append(str(n & 1))
        n >>= 1
    return "".join(reversed(bits))

if __name__ == '__main__':
    sample_values = [0, 1, 10, 255, 1024, 9999999999999999999]
    for val in sample_values:
        print(large_int_to_binary(val))