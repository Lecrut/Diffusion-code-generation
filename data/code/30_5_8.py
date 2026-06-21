def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    stack = []
    is_negative = n < 0
    n = abs(n)
    
    while n > 0:
        stack.append(n % 2)
        n = n // 2
    
    binary_digits = []
    while stack:
        binary_digits.append(str(stack.pop()))
    
    result = "".join(binary_digits)
    
    if is_negative:
        result = "-" + result
    
    return result

if __name__ == '__main__':
    print(decimal_to_binary(0))
    print(decimal_to_binary(5))
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(-42))