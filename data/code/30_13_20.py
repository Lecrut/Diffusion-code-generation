def dec_to_bin(n):
    if n == 0:
        return "0"
    sign = ""
    if n < 0:
        sign = "-"
        n = -n
    bits = []
    while n > 0:
        bits.append(str(n & 1))
        n >>= 1
    return sign + "".join(reversed(bits))

if __name__ == '__main__':
    print(dec_to_bin(10))
    print(dec_to_bin(-5))
    print(dec_to_bin(0))