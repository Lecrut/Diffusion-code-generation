def int_to_binary(n):
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(str(n & 1))
        n >>= 1
    bits.reverse()
    return "".join(bits)

if __name__ == '__main__':
    test_values = [0, 1, 2, 5, 10, 15, 16, 255, 1023, 65535]
    for value in test_values:
        result = int_to_binary(value)
        print(result)