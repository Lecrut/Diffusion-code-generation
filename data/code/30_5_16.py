def decimal_to_binary_stack(n):
    if n == 0:
        return "0"
    
    is_negative = n < 0
    n = abs(n)
    
    stack = []
    while n > 0:
        remainder = n % 2
        stack.append(remainder)
        n = n // 2
    
    binary_digits = []
    while stack:
        binary_digits.append(str(stack.pop()))
    
    result = "".join(binary_digits)
    if is_negative:
        result = "-" + result
        
    return result

if __name__ == '__main__':
    print(decimal_to_binary_stack(10))
    print(decimal_to_binary_stack(0))
    print(decimal_to_binary_stack(-5))