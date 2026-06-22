def decimal_to_binary(n):
    if n == 0:
        return "0"
    result = ""
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n
    while n > 0:
        remainder = n % 2
        result = str(remainder) + result
        n = n >> 1
    if is_negative:
        result = "-" + result
    return result

if __name__ == '__main__':
    print(decimal_to_binary(10))
    print(decimal_to_binary(0))
    print(decimal_to_binary(255))
    print(decimal_to_binary(-42))