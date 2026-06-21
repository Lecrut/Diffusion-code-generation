def int_to_binary_string(n):
    if n == 0:
        return "0"
    
    is_negative = n < 0
    n = abs(n)
    
    bits = []
    while n > 0:
        bits.append(str(n & 1))
        n >>= 1
    
    if is_negative:
        bits.append('-')
    
    bits.reverse()
    return "".join(bits)

if __name__ == '__main__':
    print(int_to_binary_string(10))
    print(int_to_binary_string(-5))
    print(int_to_binary_string(0))
    print(int_to_binary_string(255))