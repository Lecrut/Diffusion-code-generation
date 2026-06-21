def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n < 0:
        return "-" + decimal_to_binary(-n)
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n >>= 1
    return "".join(reversed(bits))

if __name__ == '__main__':
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(0))
    print(decimal_to_binary(-42))