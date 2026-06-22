def integer_to_binary_string(n):
    if n == 0:
        return "0"
    if n < 0:
        sign = "-"
        n = -n
    else:
        sign = ""
    bits = []
    while n > 0:
        bits.append(str(n & 1))
        n >>= 1
    return sign + "".join(reversed(bits))

if __name__ == '__main__':
    print(integer_to_binary_string(0))
    print(integer_to_binary_string(1))
    print(integer_to_binary_string(255))
    print(integer_to_binary_string(1024))
    print(integer_to_binary_string(123456789))
    print(integer_to_binary_string(-42))
    print(integer_to_binary_string(2**64 - 1))