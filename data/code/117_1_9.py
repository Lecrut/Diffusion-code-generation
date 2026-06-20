def abs_difference(a, b):
    return a - b if a > b else b - a

if __name__ == '__main__':
    print(abs_difference(12345678901234567890, 98765432109876543210))