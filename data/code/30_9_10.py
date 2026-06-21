def reverse_binary_conversion(n):
    if n == 0:
        return '0'
    binary_digits = []
    while n > 0:
        remainder = n % 2
        binary_digits.append(str(remainder))
        n = n // 2
    binary_string = ''.join(reversed(binary_digits))
    return binary_string

if __name__ == '__main__':
    print(reverse_binary_conversion(0))
    print(reverse_binary_conversion(1))
    print(reverse_binary_conversion(10))
    print(reverse_binary_conversion(255))
    print(reverse_binary_conversion(1024))