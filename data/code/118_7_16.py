def bitwise_multiply(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return a * b
    result = 0
    while b != 0:
        if b & 1:
            result += a
        a <<= 1
        b >>= 1
    return result

if __name__ == '__main__':
    sample_a = 7
    sample_b = 3
    print(bitwise_multiply(sample_a, sample_b))