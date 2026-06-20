def abs_difference(a, b):
    return a - b if a >= b else b - a

if __name__ == '__main__':
    result = abs_difference(12345678901234567890, 9876543210987654321)
    print(result)