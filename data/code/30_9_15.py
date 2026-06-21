def reverse_binary_conversion(n):
    if n == 0:
        return "0"
    
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n = n // 2
    
    bits.reverse()
    return "".join(bits)

if __name__ == '__main__':
    result = reverse_binary_conversion(10)
    print(result)
    result2 = reverse_binary_conversion(0)
    print(result2)
    result3 = reverse_binary_conversion(255)
    print(result3)