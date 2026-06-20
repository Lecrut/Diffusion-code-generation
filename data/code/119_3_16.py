def xor_swap(a, b):
    a = a ^ b
    if a == 0:
        return 0, 0
    b = a ^ b
    a = a ^ b
    return a, b

if __name__ == '__main__':
    x, y = 10, 20
    print(xor_swap(x, y))