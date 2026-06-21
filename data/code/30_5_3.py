def decimal_to_binary(decimal_number):
    if decimal_number < 0:
        return '-' + decimal_to_binary(-decimal_number)
    if decimal_number == 0:
        return '0'
    stack = []
    while decimal_number > 0:
        stack.append(decimal_number % 2)
        decimal_number = decimal_number // 2
    binary_digits = []
    while stack:
        binary_digits.append(str(stack.pop()))
    return ''.join(binary_digits)

if __name__ == '__main__':
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(0))
    print(decimal_to_binary(-7))