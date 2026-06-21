def decimal_to_binary(n: int) -> str:
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n = n >> 1
    return result

if __name__ == "__main__":
    sample_value = 42
    print(decimal_to_binary(sample_value))
    sample_negative = -15
    if sample_negative < 0:
        print("-" + decimal_to_binary(abs(sample_negative)))
    else:
        print(decimal_to_binary(sample_negative))
    sample_zero = 0
    print(decimal_to_binary(sample_zero))