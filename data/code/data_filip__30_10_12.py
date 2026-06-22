def int_to_binary(n):
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        if n & 1:
            result = "1" + result
        else:
            result = "0" + result
        n >>= 1
    return result

if __name__ == '__main__':
    print(int_to_binary(0))
    print(int_to_binary(5))
    print(int_to_binary(10))
    print(int_to_binary(255))
    print(int_to_binary(1024))