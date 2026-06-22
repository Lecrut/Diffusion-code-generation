def order_numbers(a, b, c):
    if not (isinstance(a, float) and isinstance(b, float) and isinstance(c, float)):
        raise ValueError("All inputs must be floating-point numbers.")
    
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    
    return a, b, c

if __name__ == '__main__':
    print(order_numbers(3.14, 2.71, 1.61))