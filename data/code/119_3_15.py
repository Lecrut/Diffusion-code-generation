def xor_swap(a, b):
    temp = a
    a = a ^ b
    b = temp ^ b
    return a, b

if __name__ == '__main__':
    x, y = 100, 200
    print(xor_swap(x, y))