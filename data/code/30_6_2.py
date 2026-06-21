def decimal_to_binary(n: int) -> str:
    if n == 0:
        return "0"
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n
    binary_digits = []
    while n > 0:
        remainder = n % 2
        binary_digits.append(str(remainder))
        n = n // 2
    binary_digits.reverse()
    result = "".join(binary_digits)
    if is_negative:
        result = "-" + result
    return result

if __name__ == '__main__':
    test_values = [0, 5, 10, 255, 1024, -42]
    for value in test_values:
        print(f"{value} -> {decimal_to_binary(value)}")