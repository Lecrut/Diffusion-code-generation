def int_to_binary(n):
    if n == 0:
        return "0"
    if n < 0:
        return "-" + int_to_binary(-n)
    bits = []
    while n > 0:
        remainder = n % 2
        bits.append(str(remainder))
        n = n // 2
    bits.reverse()
    return "".join(bits)

if __name__ == '__main__':
    test_values = [0, 1, 2, 10, 42, 255, 1024]
    for val in test_values:
        print(int_to_binary(val))