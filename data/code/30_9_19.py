def decimal_to_binary(n):
    if n == 0:
        return '0'
    negative = False
    if n < 0:
        negative = True
        n = -n
    binary_digits = []
    while n > 0:
        remainder = n % 2
        binary_digits.append(str(remainder))
        n = n // 2
    binary_digits.reverse()
    result = ''.join(binary_digits)
    if negative:
        result = '-' + result
    return result

if __name__ == '__main__':
    print(decimal_to_binary(0))
    print(decimal_to_binary(1))
    print(decimal_to_binary(2))
    print(decimal_to_binary(5))
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(-42))