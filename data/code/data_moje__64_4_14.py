def power(base, exponent):
    if exponent < 0:
        if base == 0:
            raise ValueError("0 cannot be raised to a negative power")
        return 1 / power(base, -exponent)
    
    if exponent == 0:
        return 1
    
    if exponent % 2 == 0:
        half_pow = power(base, exponent // 2)
        return half_pow * half_pow
    
    return base * power(base, exponent - 1)

if __name__ == '__main__':
    result1 = power(2, 10)
    result2 = power(3, 4)
    result3 = power(5, 0)
    result4 = power(2, 15)
    result5 = power(0.5, 3)
    result6 = power(2, -3)
    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
    print(result6)