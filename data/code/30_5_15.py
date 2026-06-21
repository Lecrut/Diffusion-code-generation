def decimal_to_binary(n):
    if n == 0:
        return '0'
    
    stack = []
    negative = False
    
    if n < 0:
        negative = True
        n = -n
    
    while n > 0:
        stack.append(str(n % 2))
        n = n // 2
    
    binary_str = ''.join(stack[::-1])
    
    if negative:
        binary_str = '-' + binary_str
    
    return binary_str

if __name__ == '__main__':
    print(decimal_to_binary(0))
    print(decimal_to_binary(5))
    print(decimal_to_binary(42))
    print(decimal_to_binary(255))
    print(decimal_to_binary(-10))