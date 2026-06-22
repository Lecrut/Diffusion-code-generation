def int_to_binary(n):
    if n == 0:
        return "0"
    result = []
    while n > 0:
        result.append(str(n & 1))
        n >>= 1
    return "".join(result[::-1])

if __name__ == '__main__':
    print(int_to_binary(0))
    print(int_to_binary(5))
    print(int_to_binary(10))
    print(int_to_binary(255))
    print(int_to_binary(1024))