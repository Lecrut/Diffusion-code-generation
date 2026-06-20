def swap_numbers(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

if __name__ == '__main__':
    x, y = 10, 20
    print(swap_numbers(x, y))