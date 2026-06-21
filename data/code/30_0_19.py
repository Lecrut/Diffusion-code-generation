def int_to_binary(n):
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n = n // 2
    return "".join(reversed(bits))

if __name__ == '__main__':
    samples = [0, 1, 5, 10, 255]
    for val in samples:
        print(int_to_binary(val))