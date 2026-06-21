def decimal_to_binary(n):
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
        n = n >> 1
    binary_digits.reverse()
    result = "".join(binary_digits)
    if is_negative:
        result = "-" + result
    return result

if __name__ == "__main__":
    sample_values = [0, 5, 10, 15, 42, -7, 255, 1024]
    for value in sample_values:
        converted = decimal_to_binary(value)
        print(f"{value}: {converted}")