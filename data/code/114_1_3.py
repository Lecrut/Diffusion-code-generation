def multiply_large_integers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    
    return a * b

if __name__ == '__main__':
    result = multiply_large_integers(12345678901234567890, 98765432109876543210)
    print(result)