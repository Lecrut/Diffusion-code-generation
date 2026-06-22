def int_to_binary(n):
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    return "".join(reversed(bits))

if __name__ == '__main__':
    print(int_to_binary(0))
    print(int_to_binary(5))
    print(int_to_binary(255))
    print(int_to_binary(1024))