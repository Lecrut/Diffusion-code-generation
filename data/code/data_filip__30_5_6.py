def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    stack = []
    negative = n < 0
    n = abs(n)
    
    while n > 0:
        remainder = n % 2
        stack.append(str(remainder))
        n = n // 2
    
    if negative:
        stack.append('-')
    
    result = ''.join(reversed(stack))
    return result

if __name__ == '__main__':
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(0))
    print(decimal_to_binary(-42))