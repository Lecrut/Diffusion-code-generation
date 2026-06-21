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
    if is_negative:
        bits.append("-")
    bits.reverse()
    return "".join(bits)

if __name__ == "__main__":
    test_values = [0, 5, 10, 15, 42, 255, 1024]
    for value in test_values:
        print(decimal_to_binary(value))
    for value in test_values:
        print(decimal_to_binary(-value))