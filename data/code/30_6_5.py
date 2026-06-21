def decimal_to_binary(n: int) -> str:
    if n == 0:
        return "0"
    if n < 0:
        return "-" + decimal_to_binary(-n)
    result = ""
    value = n
    while value > 0:
        bit = value % 2
        result = str(bit) + result
        value = value >> 1
    return result

if __name__ == '__main__':
    print(decimal_to_binary(10))
    print(decimal_to_binary(0))
    print(decimal_to_binary(255))
    print(decimal_to_binary(-42))