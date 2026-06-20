def abs_diff(x, y):
    return (x ^ y) & -(x < y)

if __name__ == '__main__':
    print(abs_diff(1234567890123456789, 9876543210987654321))