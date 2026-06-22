def decimal_to_binary(n):
    if n == 0:
        return "0b0"
    if n == 1:
        return "0b1"
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n
    binary_digits = []
    while n > 0:
        binary_digits.append(str(n % 2))
        n //= 2
    binary_digits.reverse()
    result = "0b" + "".join(binary_digits)
    if is_negative:
        result = "-" + result
    return result

if __name__ == "__main__":
    print(decimal_to_binary(0))
    print(decimal_to_binary(1))
    print(decimal_to_binary(5))
    print(decimal_to_binary(10))
    print(decimal_to_binary(-5))