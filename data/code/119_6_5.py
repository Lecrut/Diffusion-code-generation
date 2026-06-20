def reverse_numbers(a, b):
    if a == 0:
        return b
    q = b // a
    r = b % a
    x = r - (q + 1) * a
    y = a + q * x
    return y

if __name__ == '__main__':
    x = 50
    y = 30
    result_x, result_y = reverse_numbers(x, y)
    print(f"x: {result_x}, y: {result_y}")