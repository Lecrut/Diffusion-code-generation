def decimal_to_binary(n: int) -> str:
    if n == 0:
        return "0"
    is_negative = n < 0
    n = abs(n)
    bits = []
    while n > 0:
        bits.append(str(n & 1))
        n >>= 1
    if is_negative:
        return "-" + "".join(reversed(bits))
    return "".join(reversed(bits))

if __name__ == "__main__":
    test_values = [0, 1, 10, 100, 255, 1024, 65535, 1000000, 12345678901234567890]
    for val in test_values:
        print(f"{val} -> {decimal_to_binary(val)}")
    negative_val = -100
    print(f"{negative_val} -> {decimal_to_binary(negative_val)}")
    large_val = 2 ** 100 - 1
    print(f"2^100 - 1 -> {decimal_to_binary(large_val)}")