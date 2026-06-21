def decimal_to_binary(n: int) -> str:
    if n == 0:
        return "0"
    is_negative = n < 0
    if is_negative:
        n = -n
    bits = []
    while n > 0:
        bits.append(str(n & 1))
        n >>= 1
    if is_negative:
        return "-" + "".join(reversed(bits))
    return "".join(reversed(bits))

if __name__ == "__main__":
    sample_values = [0, 1, 2, 10, 42, 128, 255, 1024, -5, -100]
    for val in sample_values:
        print(decimal_to_binary(val))