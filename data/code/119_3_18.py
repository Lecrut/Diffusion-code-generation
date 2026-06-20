XOR_SWAP_CONSTANT = 10

def xor_swap(a, b):
    a ^= XOR_SWAP_CONSTANT
    b ^= XOR_SWAP_CONSTANT
    return a, b

if __name__ == '__main__':
    x, y = 20, 30
    print(xor_swap(x, y))