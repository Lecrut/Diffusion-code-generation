def decimal_to_binary_decimal(n):
    if n == 0:
        return '0'
    is_negative = n < 0
    n = abs(n)
    stack = []
    while n > 0:
        remainder = n % 2
        stack.append(str(remainder))
        n = n // 2
    binary_digits = []
    while stack:
        binary_digits.append(stack.pop())
    result = ''.join(binary_digits)
    if is_negative:
        result = '-' + result
    return result

def decimal_to_binary_hex(n):
    if n == 0:
        return '0000'
    is_negative = n < 0
    n = abs(n)
    stack = []
    while n > 0:
        remainder = n % 2
        stack.append(str(remainder))
        n = n // 2
    binary_digits = []
    while stack:
        binary_digits.append(stack.pop())
    result = ''.join(binary_digits)
    if is_negative:
        result = '-' + result
    padding_needed = 4 - (len(result) - (1 if is_negative else 0)) % 4
    if padding_needed < 4 and (len(result) - (1 if is_negative else 0)) % 4 != 0:
        if is_negative:
            result = '-' + '0' * padding_needed + result[1:]
        else:
            result = '0' * padding_needed + result
    return result
if __name__ == '__main__':
    print(decimal_to_binary_decimal(10))
    print(decimal_to_binary_decimal(0))
    print(decimal_to_binary_decimal(-5))
    print(decimal_to_binary_hex(10))
    print(decimal_to_binary_hex(0))
    print(decimal_to_binary_hex(-5))