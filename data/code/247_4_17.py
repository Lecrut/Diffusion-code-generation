def sum_large_integers(a, b):
    return a + b

if __name__ == '__main__':
    x = 12345678901234567890
    y = 98765432109876543210
    result = sum_large_integers(x, y)
    print(result)