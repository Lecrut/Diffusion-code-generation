def abs_diff(a, b):
    return a if a > b else b

if __name__ == '__main__':
    print(abs_diff(12345678901234567890, 98765432109876543210))