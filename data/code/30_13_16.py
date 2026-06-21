def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    if is_negative:
        binary = "-" + binary
    return binary

if __name__ == '__main__':
    print(decimal_to_binary(42))
    print(decimal_to_binary(0))
    print(decimal_to_binary(-15))