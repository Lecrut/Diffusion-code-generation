def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return '0'
    negative = False
    if decimal_num < 0:
        negative = True
        decimal_num = -decimal_num
    binary_digits = []
    while decimal_num > 0:
        binary_digits.append(str(decimal_num % 2))
        decimal_num //= 2
    result = ''.join(reversed(binary_digits))
    if negative:
        result = '-' + result
    return result

if __name__ == '__main__':
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(0))
    print(decimal_to_binary(-42))
    print(decimal_to_binary(10**18))