def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n < 0:
        return "-" + decimal_to_binary(-n)
    else:
        bits = []
        while n > 0:
            bits.append(str(n % 2))
            n //= 2
        return "".join(reversed(bits))

if __name__ == '__main__':
    print(decimal_to_binary(0))
    print(decimal_to_binary(5))
    print(decimal_to_binary(255))
    print(decimal_to_binary(1024))
    print(decimal_to_binary(-42))
    print(decimal_to_binary(2**64 - 1))