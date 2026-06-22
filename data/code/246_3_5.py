def add_large_integers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    
    return a + b

if __name__ == '__main__':
    num1 = 98765432109876543210
    num2 = 12345678901234567890
    result = add_large_integers(num1, num2)
    print(result)