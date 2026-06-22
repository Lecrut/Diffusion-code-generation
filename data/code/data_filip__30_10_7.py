def to_binary_string(n):
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        if n & 1:
            bits.append("1")
        else:
            bits.append("0")
        n >>= 1
    return "".join(reversed(bits))

if __name__ == '__main__':
    test_values = [0, 1, 2, 5, 10, 42, 255, 1024, 65535]
    for value in test_values:
        result = to_binary_string(value)
        print(f"{value}: {result}")