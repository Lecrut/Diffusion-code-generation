def integer_to_binary_string(n: int) -> str:
    if n == 0:
        return '0'
    
    is_negative = n < 0
    n = abs(n)
    
    bits = []
    while n > 0:
        bits.append(str(n & 1))
        n >>= 1
    
    if is_negative:
        bits.append('-')
    
    return ''.join(reversed(bits))

def integer_to_binary_string_optimized(n: int) -> str:
    if n == 0:
        return '0'
    
    if n < 0:
        return '-' + integer_to_binary_string_optimized(-n)
    
    result = []
    while n:
        result.append(str(n & 1))
        n >>= 1
    
    result.reverse()
    return ''.join(result)

if __name__ == '__main__':
    print(integer_to_binary_string(10))
    print(integer_to_binary_string(-5))
    print(integer_to_binary_string(0))
    print(integer_to_binary_string(255))
    print(integer_to_binary_string_optimized(10))
    print(integer_to_binary_string_optimized(-5))
    print(integer_to_binary_string_optimized(0))
    print(integer_to_binary_string_optimized(255))