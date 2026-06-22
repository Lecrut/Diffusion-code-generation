def fibonacci_bitwise(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibs = [0, 1]
    a = 0
    b = 1
    
    for i in range(2, n):
        c = a ^ b
        carry = a & b
        a = b
        b = c ^ (carry << 1)
        fibs.append(b)
    
    return fibs

if __name__ == '__main__':
    result = fibonacci_bitwise(100)
    for val in result:
        print(val)