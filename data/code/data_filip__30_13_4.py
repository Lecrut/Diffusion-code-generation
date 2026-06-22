def int_to_binary(n):
    if n == 0:
        return "0"
    is_negative = n < 0
    if is_negative:
        n = -n
    bits = []
    while n > 0:
        bits.append(str(n & 1))
        n >>= 1
    result = "".join(reversed(bits))
    return "-" + result if is_negative else result

if __name__ == "__main__":
    sample_value = 42
    print(int_to_binary(sample_value))
    print(int_to_binary(-13))
    print(int_to_binary(0))