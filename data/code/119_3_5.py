XOR_MASK = 0xFFFFFFFF

def swap_numbers(a, b):
    a = (a ^ b) & XOR_MASK
    b = (a ^ b) & XOR_MASK
    a = (a ^ b) & XOR_MASK
    return a, b

if __name__ == '__main__':
    x, y = 10, 20
    print(swap_numbers(x, y))