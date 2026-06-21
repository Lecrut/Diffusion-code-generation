def decimal_to_binary(n: int) -> str:
    if n < 0:
        raise ValueError("Function only supports non-negative integers")
    if n == 0:
        return "0"
    
    binary_digits = []
    while n > 0:
        binary_digits.append(str(n % 2))
        n //= 2
    
    return ''.join(reversed(binary_digits))

if __name__ == '__main__':
    print(decimal_to_binary(0))
    print(decimal_to_binary(1))
    print(decimal_to_binary(5))
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(1024))
    print(decimal_to_binary(123456789012345678901234567890))