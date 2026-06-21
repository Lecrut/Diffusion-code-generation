def decimal_to_binary(n):
    if n == 0:
        return "0b0"
    if n == 1:
        return "0b1"
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n
    result = ""
    while n > 0:
        remainder = n % 2
        result = str(remainder) + result
        n = n // 2
    if is_negative:
        return "-" + result
    return "0b" + result

if __name__ == '__main__':
    print(decimal_to_binary(0))
    print(decimal_to_binary(1))
    print(decimal_to_binary(10))
    print(decimal_to_binary(-10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(16))