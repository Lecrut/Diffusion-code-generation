def xor_swap(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    
    a = a ^ b
    b = a ^ b
    a = a ^ b
    
    return a, b

if __name__ == '__main__':
    x, y = 10, 20
    print(xor_swap(x, y))