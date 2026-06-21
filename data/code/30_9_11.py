def int_to_binary(n):
    if n == 0:
        return "0"
    is_negative = n < 0
    n = abs(n)
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n = n // 2
    bits.reverse()
    result = "".join(bits)
    if is_negative:
        result = "-" + result
    return result

if __name__ == '__main__':
    print(int_to_binary(10))
    print(int_to_binary(-5))
    print(int_to_binary(0))
    print(int_to_binary(255))