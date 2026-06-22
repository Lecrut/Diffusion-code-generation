def decimal_to_binary(n):
    if n == 0:
        return "0"
    is_negative = n < 0
    n = abs(n)
    binary_digits = []
    while n > 0:
        remainder = n % 2
        n = n >> 1
        binary_digits.append(str(remainder))
    binary_digits.reverse()
    result = "".join(binary_digits)
    if is_negative:
        result = "-" + result
    return result

if __name__ == '__main__':
    print(decimal_to_binary(10))
    print(decimal_to_binary(-5))
    print(decimal_to_binary(0))