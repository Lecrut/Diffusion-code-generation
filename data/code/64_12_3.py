def power(base, exponent):
    if exponent < 0:
        if base == 0:
            raise ZeroDivisionError("Division by zero")
        base = 1.0 / base
        exponent = -exponent
    
    if base == 0:
        return 0.0
    
    result = 1.0
    while exponent > 0:
        result *= base
        exponent -= 1
    return result

if __name__ == '__main__':
    print(power(2.0, 10))
    print(power(3.0, 3))
    print(power(2.0, -2))