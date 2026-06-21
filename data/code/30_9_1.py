def reverse_binary_conversion(n):
    if n == 0:
        return '0'
    
    bits = []
    num = n
    while num > 0:
        bits.append(str(num % 2))
        num //= 2
    
    return ''.join(reversed(bits))

if __name__ == '__main__':
    print(reverse_binary_conversion(10))
    print(reverse_binary_conversion(0))
    print(reverse_binary_conversion(255))
    print(reverse_binary_conversion(42))