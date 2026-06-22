def reverse_binary_conversion(n):
    if n == 0:
        return "0"
    
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    bits = []
    temp = n
    while temp > 0:
        bits.append(str(temp % 2))
        temp //= 2
    
    bits.reverse()
    return "".join(bits)

if __name__ == '__main__':
    print(reverse_binary_conversion(10))
    print(reverse_binary_conversion(255))
    print(reverse_binary_conversion(0))
    print(reverse_binary_conversion(7))