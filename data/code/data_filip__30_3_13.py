def integer_to_binary_string(n: int) -> str:
    if n == 0:
        return "0"
    
    is_negative = n < 0
    if is_negative:
        n = -n
    
    if n == 0:
        return "0"
    
    bits = []
    while n > 0:
        bits.append('1' if n & 1 else '0')
        n >>= 1
    
    if is_negative:
        return "~" + "".join(reversed(bits))
    
    return "".join(reversed(bits))

if __name__ == '__main__':
    print(integer_to_binary_string(0))
    print(integer_to_binary_string(1))
    print(integer_to_binary_string(10))
    print(integer_to_binary_string(255))
    print(integer_to_binary_string(-10))