def int_to_binary(n: int) -> str:
    if n == 0:
        return "0"
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n
    bits = []
    while n > 0:
        bits.append('1' if n & 1 else '0')
        n >>= 1
    bits.reverse()
    result = ''.join(bits)
    return '-' + result if is_negative else result

if __name__ == '__main__':
    print(int_to_binary(10))
    print(int_to_binary(-5))
    print(int_to_binary(0))
    print(int_to_binary(255))