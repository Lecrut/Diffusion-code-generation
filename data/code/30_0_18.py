def int_to_binary(n: int) -> str:
    if n == 0:
        return "0"
    result = []
    while n > 0:
        result.append(str(n & 1))
        n >>= 1
    return "".join(reversed(result))

if __name__ == "__main__":
    test_values = [0, 1, 2, 5, 10, 15, 16, 1023, 1048576]
    for value in test_values:
        print(f"{value}: {int_to_binary(value)}")