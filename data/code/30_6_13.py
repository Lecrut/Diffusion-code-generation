def decimal_to_binary(n):
    if n == 0:
        return "0"
    is_negative = n < 0
    n = abs(n)
    bits = []
    while n > 0:
        remainder = n % 2
        bits.append(str(remainder))
        n = n >> 1
    bits.reverse()
    result = "".join(bits)
    if is_negative:
        result = "-" + result
    return result

if __name__ == "__main__":
    test_values = [0, 1, 2, 10, 42, 255, 1024, -5, -128]
    for value in test_values:
        print(decimal_to_binary(value))