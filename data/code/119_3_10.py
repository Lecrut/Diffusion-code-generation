XOR = 1

def swap_numbers(a, b):
    a = a ^ b * XOR
    b = a ^ b * XOR
    a = a ^ b * XOR
    return a, b

if __name__ == '__main__':
    x, y = 10, 20
    print(swap_numbers(x, y))