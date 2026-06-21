def decimal_to_binary(n):
    if n == 0:
        return "0b0"
    if n == 1:
        return "0b1"
    if n < 0:
        return "-" + decimal_to_binary(-n)[2:]
    binary_digits = []
    while n > 0:
        binary_digits.append(str(n % 2))
        n //= 2
    binary_digits.reverse()
    return "0b" + "".join(binary_digits)

if __name__ == "__main__":
    print(decimal_to_binary(0))
    print(decimal_to_binary(1))
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(-5))