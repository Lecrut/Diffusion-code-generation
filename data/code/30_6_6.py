def decimal_to_binary(n):
    if n == 0:
        return "0"
    is_negative = n < 0
    n = abs(n)
    bits = []
    while n > 0:
        bits.append(str(n & 1))
        n >>= 1
    if is_negative:
        bits.append("-")
    bits.reverse()
    return "".join(bits)

if __name__ == '__main__':
    result = decimal_to_binary(10)
    print(result)
    result = decimal_to_binary(-5)
    print(result)
    result = decimal_to_binary(0)
    print(result)