def decimal_to_binary(n):
    if n == 0:
        return "0"
    bits = []
    is_negative = n < 0
    n = abs(n)
    while n > 0:
        remainder = n % 2
        bits.append(str(remainder))
        n = n >> 1
    if is_negative:
        bits.append("-")
    bits.reverse()
    return "".join(bits)

if __name__ == '__main__':
    print(decimal_to_binary(10))
    print(decimal_to_binary(-5))
    print(decimal_to_binary(0))