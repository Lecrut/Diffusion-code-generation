def decimal_to_binary(number):
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    if number == 0:
        return "0"
    is_negative = number < 0
    number = abs(number)
    result = []
    while number > 0:
        result.append(str(number & 1))
        number >>= 1
    binary_str = "".join(reversed(result))
    return "-" + binary_str if is_negative else binary_str

if __name__ == '__main__':
    print(decimal_to_binary(10))
    print(decimal_to_binary(0))
    print(decimal_to_binary(255))
    print(decimal_to_binary(-42))
    print(decimal_to_binary(1024))
    print(decimal_to_binary(-1024))
    print(decimal_to_binary(2**100))