def multiply(a, b):
    if isinstance(a, int) and isinstance(b, int):
        result = 0
        negative_result = False
        if a < 0:
            a = -a
            negative_result = not negative_result
        if b < 0:
            b = -b
            negative_result = not negative_result
        while b > 0:
            if b & 1 == 1:
                result += a
            a <<= 1
            b >>= 1
        return result if not negative_result else -result
    else:
        return a * b
if __name__ == '__main__':
    print(multiply(5, 3))
    print(multiply(-5, 3))
    print(multiply(-4, -2))
    print(multiply(0, 5))