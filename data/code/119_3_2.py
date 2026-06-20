def xor_swap(a, b):
    temp = a
    a = a ^ b
    b = temp ^ b
    return a, b

if __name__ == '__main__':
    x, y = 30, 45
    print(xor_swap(x, y))