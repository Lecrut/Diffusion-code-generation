XOR_SWAP_MASK = 0xFFFFFFFF

def xor_swap(a, b):
    a = (a ^ b) & XOR_SWAP_MASK
    b = (b ^ a) & XOR_SWAP_MASK
    a = (a ^ b) & XOR_SWAP_MASK
    return a, b

if __name__ == '__main__':
    x, y = 10, 20
    print(xor_swap(x, y))